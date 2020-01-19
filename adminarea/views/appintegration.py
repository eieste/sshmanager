from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from partitialajax.mixin import ListPartitialAjaxMixin, CreatePartitialAjaxMixin, DetailPartitialAjaxMixin, DeletePartitialAjaxMixin
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from adminarea.models import AppIntegration
from adminarea.forms import AppIntegrationForm


class AppIntegrationListView(LoginRequiredMixin, ListPartitialAjaxMixin, ListView):
    template_name = "adminarea/appintegration/list.html"
    model = AppIntegration
    partitial_list = {
        "tbody#appintegration-list-partitial": "adminarea/appintegration/partitial/list.html",
    }


class AppIntegrationCreateView(LoginRequiredMixin, CreatePartitialAjaxMixin, CreateView):
    template_name = "adminarea/appintegration/create.html"
    form_class = AppIntegrationForm
    #permission_required = ("adminarea.add_appintegration",)
    partitial_list = {
        ".modal-content": "adminarea/appintegration/partitial/create.html",
    }

    def get_success_url(self):
        return reverse_lazy("adminarea:appintegration:detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.organization = self.request.user.organization
        return super(AppIntegrationCreateView, self).form_valid(form)



class AppIntegrationDeleteView(LoginRequiredMixin, DeletePartitialAjaxMixin, DeleteView):
    template_name = "adminarea/appintegration/delete.html"
    model = AppIntegration
    partitial_list = {
        ".modal-content": "adminarea/appintegration/partitial/delete.html"
    }

    def get_success_url(self):
        return reverse_lazy("adminarea:appintegration:list")

class AppIntegrationDetailView(LoginRequiredMixin, DetailView):
    template_name = "adminarea/appintegration/detail.html"
    model = AppIntegration