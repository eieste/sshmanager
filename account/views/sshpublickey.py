from django.views.generic import TemplateView, ListView, DetailView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from account.models import KeyGroup, SSHPublicKey, SSHPublicKeyToKeyGroup
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from account.forms import SSHPublicKeyCreateForm, AssignKeyGroupToSSHPublicKeyForm
import hashlib
from sshmanager.contrib import get_master_user
from Crypto.PublicKey import RSA
import base64
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib import messages


class SSHPublicKeyListView(LoginRequiredMixin, ListView):
    template_name = "account/sshpublickey/sshpublickey_list.html"
    model = SSHPublicKey

    def get_queryset(self):
        qs = super(SSHPublicKeyListView, self).get_queryset()

        return qs.filter(created_by=self.request.user)


class SSHPublicKeyCreateView(LoginRequiredMixin, CreateView):
    template_name = "account/sshpublickey/sshpublickey_create.html"
    model = SSHPublicKey
    form_class = SSHPublicKeyCreateForm
    success_url = reverse_lazy("account:sshpublickey:list")

    def get_form(self, form_class=None):
        form = super(SSHPublicKeyCreateView, self).get_form(form_class)
        form.fields["key_groups"].queryset = KeyGroup.objects.filter(created_by__in=[self.request.user, get_master_user()])
        return form

    def form_valid(self, form):
        form.instance.created_by = self.request.user

        key = RSA.importKey(form.instance.ssh_public_key)
        openssh_key = key.export_key("OpenSSH")
        openssh_key_bytes_string = openssh_key.decode("utf-8").split(" ")

        openssh_key_bytes = base64.b64decode(openssh_key_bytes_string[1].encode("ascii"))

        dig = hashlib.sha256()
        dig.update(openssh_key_bytes)
        openssh_fingerprint = base64.b64encode(dig.digest()).decode("ascii").replace("=", "")
        form.instance.fingerprint = f"{key.size_in_bits()} SHA265: {openssh_fingerprint}"
        return super(SSHPublicKeyCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except IntegrityError:
            messages.add_message(request, messages.ERROR,
                                 'You already have registered a Client with this name. ' + \
                                 'All of your Client names must be unique.')
            return self.render_to_response(context=self.get_context_data())


class SSHPublicKeyDetailView(LoginRequiredMixin, DetailView):
    template_name = "account/sshpublickey/sshpublickey_detail.html"
    model = SSHPublicKey


class SSHPublicKeyDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ["account.delete_sshpublickey"]
    template_name = "account/sshpublickey/sshpublickey_delete.html"
    model = SSHPublicKey
    success_url = reverse_lazy("account:sshpublickey:list")


class DissociateKeyGroupToSSHPublicKeyView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = SSHPublicKeyToKeyGroup
    permission_required = ["account.delete_sshpublickeytokeygroup"]
    template_name = "account/sshpublickey/sshpublickey_dissociate_keygroup.html"

    def get_success_url(self):
        # Assuming there is a ForeignKey from Comment to Post in your model
        ssh_public_key = self.object.ssh_public_key
        return reverse_lazy( 'account:sshpublickey:detail', kwargs={'pk': ssh_public_key.pk})


class AssignKeyGroupToSSHPublicKeyView(LoginRequiredMixin, FormView):
    # template_name = "account/sshpublickey/"
    form_class = AssignKeyGroupToSSHPublicKeyForm
    template_name = "account/sshpublickey/sshpublickey_assign_keygroup.html"

    def get_object(self):
        return SSHPublicKey.objects.get(pk=self.kwargs["pk"])

    def get_success_url(self):
        return reverse_lazy("account:sshpublickey:detail", args=[self.get_object().pk])

    def get_form(self, form_class=None):
        form = super(AssignKeyGroupToSSHPublicKeyView, self).get_form()
        form.fields["key_groups"].queryset = KeyGroup.objects.filter(created_by__in=[self.request.user, get_master_user()], sshpublickeytokeygroup__isnull=True)
        return form

    def form_valid(self, form):
        key_groups = form.cleaned_data.get("key_groups", [])

        for key_group in key_groups:
            SSHPublicKeyToKeyGroup.objects.get_or_create(key_group=key_group, ssh_public_key=self.get_object(), created_by=self.request.user)

        return redirect(self.get_success_url())