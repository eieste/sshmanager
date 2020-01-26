from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView
from django.utils.translation import pgettext
from partitialajax.mixin import DeletePartitialAjaxMixin, CreatePartitialAjaxMixin, ListPartitialAjaxMixin
from sshock.contrib.mixins import PartitialFormMixin
from superarea.models import Host
from django.urls import reverse_lazy


class HostCreateView(LoginRequiredMixin, PartitialFormMixin, CreatePartitialAjaxMixin, CreateView):
    model = Host
    fields = ("host", "user")
    success_url = reverse_lazy("superarea:host:list")
    partitial_form_url = reverse_lazy("superarea:host:create")
    partitial_bundle_name = "superarea_host_create"
    partitial_form_title = pgettext("Modal Title", "Create Host")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.organization = self.request.user.organization
        return super(HostCreateView, self).form_valid(form)


class HostDeleteView(LoginRequiredMixin, PartitialFormMixin, DeletePartitialAjaxMixin, DeleteView):
    model = Host
    success_url = reverse_lazy("superarea:host:list")
    partitial_form_url = reverse_lazy("superarea:host:delete")
    partitial_bundle_name = "superarea_host_delete"
    partitial_form_title = pgettext("Modal Title", "Delete Host")


class HostListView(LoginRequiredMixin, ListPartitialAjaxMixin, ListView):
    template_name = "superarea/host/list.html"
    model = Host
    partitial_list = {
        "tbody#host-list-partitial": "superarea/host/partitial/list.html"
    }

    def get_queryset(self):
        return self.request.user.host_set.all()