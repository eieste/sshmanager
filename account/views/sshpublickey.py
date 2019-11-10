from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from account.models import KeyGroup, SSHPublicKey
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from account.forms import SSHPublicKeyCreateForm
import hashlib
from Crypto.PublicKey import RSA
import base64


class SSHPublicKeyListView(LoginRequiredMixin, ListView):
    template_name = "account/sshpublickey/sshpublickey_list.html"
    model = SSHPublicKey


class SSHPublicKeyCreateView(LoginRequiredMixin, CreateView):
    template_name = "account/sshpublickey/sshpublickey_create.html"
    model = SSHPublicKey
    form_class = SSHPublicKeyCreateForm
    success_url = reverse_lazy("sshpublickey:list")

    def form_valid(self, form):
        form.instance.user = self.request.user

        key = RSA.importKey(form.instance.key)
        openssh_key = key.export_key("OpenSSH")
        openssh_key_bytes_string = openssh_key.decode("utf-8").split(" ")

        openssh_key_bytes = base64.b64decode(openssh_key_bytes_string[1].encode("ascii"))

        dig = hashlib.sha256()
        dig.update(openssh_key_bytes)
        openssh_fingerprint = base64.b64encode(dig).decode("ascii").replace("=", "")
        form.instance.fingerprint = f"{key.size_in_bits()} SHA265: {openssh_fingerprint}"
        return super(SSHPublicKeyCreateView, self).form_valid(form)