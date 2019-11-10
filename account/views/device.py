from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView

from account.models import Device


class DeviceListView(LoginRequiredMixin, ListView):
    template_name = "account/device/device_list.html"
    model = Device


class DeviceCreateView(LoginRequiredMixin, CreateView):
    template_name = "account/device/device_create.html"
    model = Device
    success_url = reverse_lazy("device:list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DeviceCreateView, self).form_valid(form)