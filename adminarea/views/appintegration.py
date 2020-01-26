from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from partitialajax.mixin import ListPartitialAjaxMixin, CreatePartitialAjaxMixin, DetailPartitialAjaxMixin, DeletePartitialAjaxMixin
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from adminarea.models import AppIntegration
from adminarea.forms import AppIntegrationForm
from django.utils.translation import pgettext
from sshock.contrib.mixins import PartitialFormMixin


class AppIntegrationListView(LoginRequiredMixin, ListPartitialAjaxMixin, ListView):
    template_name = "adminarea/appintegration/list.html"
    model = AppIntegration
    partitial_list = {
        "tbody#appintegration-list-partitial": "adminarea/appintegration/partitial/list.html",
    }


class AppIntegrationCreateView(LoginRequiredMixin, PartitialFormMixin, CreatePartitialAjaxMixin, CreateView):
    form_class = AppIntegrationForm
    partitial_form_url = reverse_lazy("adminarea:appintegration:create")
    partitial_bundle_name = "adminarea_appintegration_create"
    partitial_form_title = pgettext("Modal Title", "Create App-Integration")
    partitial_cancel_url = reverse_lazy("adminarea:appintegration:list")

    def get_success_url(self):
        return reverse_lazy("adminarea:appintegration:detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.organization = self.request.user.organization
        return super(AppIntegrationCreateView, self).form_valid(form)


class AppIntegrationDeleteView(LoginRequiredMixin, PartitialFormMixin, DeletePartitialAjaxMixin, DeleteView):
    model = AppIntegration
    partitial_form_url = reverse_lazy("adminarea:appintegration:delete")
    partitial_bundle_name = "adminarea_appintegration_delete"
    partitial_form_title = pgettext("Modal Title", "Delete App-Integration")
    partitial_cancel_url = reverse_lazy("adminarea:appintegration:list")


    def get_success_url(self):
        return reverse_lazy("adminarea:appintegration:list")


class AppIntegrationDetailView(LoginRequiredMixin, DetailView):
    template_name = "adminarea/appintegration/detail.html"
    model = AppIntegration