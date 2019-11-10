from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from account.models import Device, KeyGroup
from sshmanager.contrib import get_master_user


class DeviceAndGroupListView(LoginRequiredMixin, TemplateView):
    template_name = "account/group/list.html"

    def get_context_data(self, **kwargs):
        ctx = super(DeviceAndGroupListView, self).get_context_data(**kwargs)
        ctx["device_list"] = self.request.user.device_set.all() | Device.objects.filter(user=get_master_user())
        ctx["keygroup_list"] = self.request.user.keygroup_set.all() | KeyGroup.objects.filter(user=get_master_user())
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