from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView, DeleteView, ListView
from partitialajax.mixin import PartitialAjaxMixin, DeletePartitialAjaxMixin, ListPartitialAjaxMixin, CreatePartitialAjaxMixin
from userarea.forms import DeviceCreateForm
from userarea.models import Device


class DeviceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreatePartitialAjaxMixin, CreateView):
    permission_required = ["userarea.add_device"]
    template_name = "userarea/device/create.html"
    model = Device
    form_class = DeviceCreateForm
    success_url = reverse_lazy("userarea:device:list")

    partitial_list = {
        ".modal-content": "userarea/device/partitial/create.html"
    }

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.organization = self.request.user.organization
        form.instance.name = slugify(form.cleaned_data.get("display_name"))
        return super(DeviceCreateView, self).form_valid(form)


class DeviceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeletePartitialAjaxMixin, DeleteView):
    permission_required = ["userarea.delete_device"]
    template_name = "userarea/device/delete.html"
    model = Device
    success_url = reverse_lazy("userarea:device:list")
    partitial_list = {
        ".modal-content": "userarea/device/partitial/delete.html"
    }


class DeviceListView(LoginRequiredMixin, PermissionRequiredMixin, ListPartitialAjaxMixin, ListView):
    permission_required = ["userarea.view_device"]
    model = Device
    template_name = "userarea/device/list.html"

    partitial_list = {
        "tbody#device-list-partitial": "userarea/device/partitial/list.html"
    }

    def get_queryset(self, *args, **kwargs):
        return Device.filter_by_visibility(self.request)