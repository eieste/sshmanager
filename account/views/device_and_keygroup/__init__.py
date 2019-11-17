from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView
from account.models import Device
from account.models import KeyGroup
from sshmanager.contrib import get_master_user
from .device import DeviceCreateView
from .keygroup import KeyGroupCreateView, KeyGroupDetailView, KeyGroupDeleteView


class DeviceAndGroupListView(LoginRequiredMixin, TemplateView):
    template_name = "account/device_and_keygroup/list.html"

    def get_context_data(self, **kwargs):
        ctx = super(DeviceAndGroupListView, self).get_context_data(**kwargs)

        if self.request.user.has_perm("account.view_device"):
            ctx["device_list"] = self.request.user.device_set.all() | Device.objects.filter(created_by=get_master_user())

        if self.request.user.has_perm("account.view_keygroup"):
            ctx["keygroup_list"] = self.request.user.keygroup_set.all() | KeyGroup.objects.filter(created_by=get_master_user())

        return ctx
