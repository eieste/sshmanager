from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView

from account.models import Device, KeyGroup
from sshmanager.contrib import get_master_user


class DeviceAndGroupListView(LoginRequiredMixin, TemplateView):
    template_name = "account/device_and_keygroup/list.html"

    def get_context_data(self, **kwargs):
        ctx = super(DeviceAndGroupListView, self).get_context_data(**kwargs)

        if self.request.user.has_perm("account.view_device"):
            ctx["device_list"] = self.request.user.device_set.all() | Device.objects.filter(created_by=get_master_user())

        if self.request.user.has_perm("account.view_keygroup"):
            ctx["keygroup_list"] = self.request.user.keygroup_set.all() | KeyGroup.objects.filter(created_by=get_master_user())

        return ctx

"""
class DeviceCreateView(LoginRequiredMixin, CreateView):
    template_name = "account/device/device_create.html"
    model = Device
    form_class = DeviceForm
    success_url = reverse_lazy("device:list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.name = form.display_name
        return super(DeviceCreateView, self).form_valid(form)
"""