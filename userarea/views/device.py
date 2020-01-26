from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView, DeleteView, ListView
from partitialajax.mixin import PartitialAjaxMixin, DeletePartitialAjaxMixin, ListPartitialAjaxMixin, CreatePartitialAjaxMixin
from userarea.forms import DeviceCreateForm
from userarea.models import Device
from django.utils.translation import pgettext
from sshock.contrib.mixins import PartitialFormMixin


class DeviceCreateView(LoginRequiredMixin, PartitialFormMixin, CreatePartitialAjaxMixin, CreateView):
    model = Device
    form_class = DeviceCreateForm
    success_url = reverse_lazy("userarea:device:list")
    partitial_form_url = reverse_lazy("userarea:device:create")
    partitial_bundle_name = "userarea_device_create"
    partitial_form_title = pgettext("Modal Title", "Create Device")
    partitial_cancel_url = reverse_lazy("userarea:device:list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.organization = self.request.user.organization
        form.instance.name = slugify(form.cleaned_data.get("display_name"))
        return super(DeviceCreateView, self).form_valid(form)


class DeviceDeleteView(LoginRequiredMixin, PartitialFormMixin, DeletePartitialAjaxMixin, DeleteView):
    model = Device
    success_url = reverse_lazy("userarea:device:list")
    partitial_singleobject_form_url = "userarea:device:delete"
    partitial_bundle_name = "userarea_device_delete"
    partitial_form_title = pgettext("Modal Title", "Delete Device")
    partitial_cancel_url = reverse_lazy("userarea:device:list")


class DeviceListView(LoginRequiredMixin, ListPartitialAjaxMixin, ListView):
    model = Device
    template_name = "userarea/device/list.html"

    partitial_list = {
        "tbody#device-list-partitial": "userarea/device/partitial/list.html"
    }

    def get_queryset(self, *args, **kwargs):
        return Device.filter_by_visibility(self.request)