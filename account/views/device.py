from django.contrib.auth.mixins import LoginRequiredMixin
import hashlib

from Crypto.PublicKey import RSA
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from account.forms import DeviceCreateForm
from account.models import Device


class DeviceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ["account.add_device"]
    template_name = "account/device_and_keygroup/device/device_create.html"
    model = Device
    form_class = DeviceCreateForm
    success_url = reverse_lazy("device-and-keygroup:list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DeviceCreateView, self).form_valid(form)

