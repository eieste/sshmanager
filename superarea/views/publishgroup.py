from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from partitialajax.mixin import *

from superarea.models import PublishGroup


class PublishGroupCreateView(LoginRequiredMixin, CreatePartitialAjaxMixin, CreateView):
    template_name = "superarea/publishgroup/create.html"
    model = PublishGroup
    fields = ("display_name",)
    partitial_list = {
        ".modal-content": "superarea/publishgroup/partitial/create.html"
    }

    def get_success_url(self):
        return reverse_lazy("superarea:publishgroup:detail", args=[self.object.pk])

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(PublishGroupCreateView, self).form_valid(form)


class PublishGroupListView(LoginRequiredMixin, ListPartitialAjaxMixin, ListView):
    template_name = "superarea/publishgroup/list.html"
    model = PublishGroup
    partitial_list = {
        "tbody#publishgroup-partitial": "superarea/publishgroup/partitial/list.html"
    }


class PublishGroupDetailView(LoginRequiredMixin, ListView):
    template_name = "superarea/publishgroup/detail.html"
    model = PublishGroup


class PublishGroupDeleteView(LoginRequiredMixin, DeletePartitialAjaxMixin, DeleteView):
    template_name = "superarea/publishgroup/delete.html"
    model = PublishGroup
    partitial_list = {
        ".modal-content": "superarea/publishgroup/partitial/delete.html"
    }

    def get_success_url(self):
        return reverse_lazy("superarea:publishgroup:list")


