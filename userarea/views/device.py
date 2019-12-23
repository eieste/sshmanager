from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView, DeleteView, ListView

from userarea.forms import DeviceCreateForm
from userarea.models import Device


class DeviceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ["userarea.add_device"]
    template_name = "userarea/device/create.html"
    model = Device
    form_class = DeviceCreateForm
    success_url = reverse_lazy("account:device-and-keygroup:list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.name = slugify(form.cleaned_data.get("display_name"))
        return super(DeviceCreateView, self).form_valid(form)


class DeviceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ["userarea.delete_device"]
    template_name = "userarea/device/delete.html"
    model = Device
    success_url = reverse_lazy("account:device:list")


class DeviceListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ["userarea.view_device"]
    model = Device
    template_name = "userarea/device/list.html"

    def get_queryset(self, *args, **kwargs):
        queryset = super(DeviceListView, self).get_queryset(*args, **kwargs)
        return queryset