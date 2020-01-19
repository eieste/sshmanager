import base64
import hashlib

from Crypto.PublicKey import RSA
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import IntegrityError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView, DetailView, DeleteView, FormView
from partitialajax.mixin import ListPartitialAjaxMixin, CreatePartitialAjaxMixin, DeletePartitialAjaxMixin
from userarea.forms import PublicKeyCreateForm, AssignKeyGroupToPublicKeyForm
from userarea.models import KeyGroup, PublicKey, PublicKeyToKeyGroup
from sshock.contrib import get_master_user


class PublicKeyListView(LoginRequiredMixin, ListPartitialAjaxMixin, ListView):
    template_name = "userarea/publickey/list.html"
    model = PublicKey
    partitial_list = {
        "tbody#publickey-list-partitial": "userarea/publickey/partitial/list.html"
    }

    def get_queryset(self):
        qs = super(PublicKeyListView, self).get_queryset()
        return qs.filter(created_by=self.request.user)


class PublicKeyCreateView(LoginRequiredMixin, CreatePartitialAjaxMixin, CreateView):
    template_name = "userarea/publickey/create.html"
    model = PublicKey
    form_class = PublicKeyCreateForm
    success_url = reverse_lazy("userarea:publickey:list")
    partitial_list = {
        ".modal-content": "userarea/publickey/partitial/create.html"
    }

    def get_form(self, form_class=None):
        form = super(PublicKeyCreateView, self).get_form(form_class)
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
        return super(PublicKeyCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except IntegrityError:
            messages.add_message(request, messages.ERROR,
                                 'You already have registered a Key with this fingerprint. ' + \
                                 'All of your Public-Keys must be unique.')
            return self.render_to_response(context=self.get_context_data())


class PublicKeyDetailView(LoginRequiredMixin, DetailView):
    template_name = "userarea/publickey/detail.html"
    model = PublicKey


class PublicKeyDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ["userarea.delete_publickey"]
    template_name = "userarea/publickey/delete.html"
    model = PublicKey
    success_url = reverse_lazy("account:publickey:list")
