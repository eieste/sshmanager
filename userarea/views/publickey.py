import base64
import hashlib

from Crypto.PublicKey import RSA
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import IntegrityError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView, DetailView, DeleteView, FormView, UpdateView
from partitialajax.mixin import ListPartitialAjaxMixin, CreatePartitialAjaxMixin, DeletePartitialAjaxMixin, DetailPartitialAjaxMixin, UpdatePartitialAjaxMixin
from userarea.forms import PublicKeyCreateForm, AssignKeyGroupToPublicKeyForm
from userarea.models import KeyGroup, PublicKey, PublicKeyToKeyGroup
from sshock.contrib import get_master_user
from sshock.contrib.mixins import PartitialFormMixin
from django.utils.translation import pgettext


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
    model = PublicKey
    form_class = PublicKeyCreateForm
    success_url = reverse_lazy("userarea:publickey:list")
    template_name = "userarea/publickey/create.html"
    partitial_list = {
        "#publickey-create-device-field": "userarea/publickey/partitial/field_device.html",
        "#publickey-create-key-group-field": "userarea/publickey/partitial/field_key_group.html",
        ".card-body#publickey-create-partitial": "userarea/publickey/partitial/create.html",

    }

    def get_form(self, form_class=None):
        form = super(PublicKeyCreateView, self).get_form(form_class)
        form.fields["key_group"].queryset = KeyGroup.objects.filter(created_by=self.request.user)
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
        self.object = form.save()

        for relation in form.cleaned_data["key_groups"]:
            PublicKeyToKeyGroup.objects.create(key_group=relation, public_key=self.object)

        return self.get_success_url()

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except IntegrityError:
            messages.add_message(request, messages.ERROR,
                                 'You already have registered a Key with this fingerprint. ' + \
                                 'All of your Public-Keys must be unique.')
            return self.render_to_response(context=self.get_context_data())


class PublicKeyDetailView(LoginRequiredMixin, UpdatePartitialAjaxMixin, UpdateView):
    template_name = "userarea/publickey/update.html"
    model = PublicKey
    fields = ("name", )
    partitial_list = {
        ".modal-content": "userarea/publickey/partitial/update.html"
    }


class PublicKeyDeleteView(LoginRequiredMixin, PartitialFormMixin, DeletePartitialAjaxMixin, DeleteView):
    model = PublicKey
    success_url = reverse_lazy("userarea:publickey:list")
    partitial_singleobject_form_url = "userarea:publickey:delete"
    partitial_bundle_name = "userarea_publickey_delete"
    partitial_form_title = pgettext("Modal Title", "Delete Publickey")
    partitial_cancel_url = reverse_lazy("userarea:publickey:list")