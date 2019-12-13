from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, FormView, DeleteView
from publish.models import PublishGroup, PublishGroupToKeyGroup
from account.models import KeyGroup
from django.urls import reverse_lazy
from publish.forms import PublishGroupToKeyGroupForm
from sshock.contrib import get_master_user
from django.forms import formset_factory
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class PublishGroupCreateView(LoginRequiredMixin, CreateView):
    template_name = "publish/publishgroup/publishgroup_create.html"
    model = PublishGroup
    fields = ("display_name",)

    def get_success_url(self):
        return reverse_lazy("publish:publishgroup:detail", args=[self.object.pk])

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(PublishGroupCreateView, self).form_valid(form)


class PublishGroupListView(LoginRequiredMixin, ListView):
    template_name = "publish/publishgroup/publishgroup_list.html"
    model = PublishGroup


class PublishGroupDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "publish/publishgroup/publishgroup_delete.html"
    model = PublishGroup

    def get_success_url(self):
        return reverse_lazy("publish:publishgroup:list")


