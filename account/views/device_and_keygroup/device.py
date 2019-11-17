from account.forms import DeviceCreateForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from account.forms import DeviceCreateForm
from account.models import Device


class DeviceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ["account.add_device"]
    template_name = "account/device_and_keygroup/device/device_create.html"
    model = Device
    form_class = DeviceCreateForm
    success_url = reverse_lazy("account:device-and-keygroup:list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(DeviceCreateView, self).form_valid(form)

