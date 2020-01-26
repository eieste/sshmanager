from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView
from superarea.models import HostGroup
from django.utils.translation import pgettext
from sshock.contrib.mixins import PartitialFormMixin
from partitialajax.mixin import CreatePartitialAjaxMixin, ListPartitialAjaxMixin, DeletePartitialAjaxMixin
from django.urls import reverse_lazy
from django.utils.text import slugify

class HostGroupCreateView(LoginRequiredMixin, PartitialFormMixin, CreatePartitialAjaxMixin, CreateView):
    model = HostGroup
    fields = ("display_name",)
    partitial_form_url = reverse_lazy("superarea:hostgroup:create")
    partitial_bundle_name = "superarea_hostgroup_create"
    partitial_form_title = pgettext("Modal Title", "Create Hostgroup")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.organization = self.request.user.organization
        form.instance.name = slugify(form.cleaned_data.get("display_name"))
        return super(HostGroupCreateView, self).form_valid(form)


class HostGroupDeleteView(LoginRequiredMixin, PartitialFormMixin, DeletePartitialAjaxMixin, DeleteView):
    model = HostGroup
    partitial_form_url = reverse_lazy("superarea:hostgroup:delete")
    partitial_bundle_name = "superarea_hostgroup_delete"
    partitial_form_title = pgettext("Modal Title", "Delete Hostgroup")


class HostGroupListView(LoginRequiredMixin, ListPartitialAjaxMixin, ListView):
    template_name = "superarea/hostgroup/list.html"
    model = HostGroup
    partitial_list = {
        "tbody#hostgroup-list-partitial": "superarea/hostgroup/partitial/list.html"
    }