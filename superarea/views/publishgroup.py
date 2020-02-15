from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from partitialajax.mixin import CreatePartitialAjaxMixin, ListPartitialAjaxMixin, DeletePartitialAjaxMixin, UpdatePartitialAjaxMixin
from django.utils.translation import pgettext
from sshock.contrib.mixins import PartitialFormMixin
from superarea.models import PublishGroup


class PublishGroupCreateView(LoginRequiredMixin, PartitialFormMixin, CreatePartitialAjaxMixin, CreateView):
    model = PublishGroup
    fields = ("display_name", "organizational_visibility")
    partitial_form_url = reverse_lazy("superarea:publishgroup:create")
    partitial_bundle_name = "superarea_publishgroup_create"
    partitial_form_title = pgettext("Modal Title", "Create Publishgroup")
    partitial_cancel_url = reverse_lazy("superarea:publishgroup:create")

    def get_success_url(self):
        return reverse_lazy("superarea:publishgroup:detail", args=[self.object.pk])

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.organization = self.request.user.organization
        return super(PublishGroupCreateView, self).form_valid(form)


class PublishGroupListView(LoginRequiredMixin, ListPartitialAjaxMixin, ListView):
    template_name = "superarea/publishgroup/list.html"
    model = PublishGroup
    partitial_list = {
        "tbody#publishgroup-partitial": "superarea/publishgroup/partitial/list.html"
    }


class PublishGroupDeleteView(LoginRequiredMixin, PartitialFormMixin, DeletePartitialAjaxMixin, DeleteView):
    model = PublishGroup
    partitial_form_url = reverse_lazy("superarea:publishgroup:delete")
    partitial_bundle_name = "superarea_publishgroup_delete"
    partitial_form_title = pgettext("Modal Title", "Delete Publishgroup")
    partitial_cancel_url = reverse_lazy("superarea:publishgroup:delete")

    def get_success_url(self):
        return reverse_lazy("superarea:publishgroup:list")


