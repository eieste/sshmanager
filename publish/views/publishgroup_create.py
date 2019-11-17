from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, FormView
from publish.models import PublishGroup, PublishGroupToKeyGroup
from account.models import KeyGroup
from django.urls import reverse_lazy
from publish.forms import PublishGroupToKeyGroupForm
from sshmanager.contrib import get_master_user
from django.forms import formset_factory
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class PublishGroupCreateView(LoginRequiredMixin, CreateView):
    template_name = "publish/group/create.html"
    model = PublishGroup
    fields = ("display_name",)
    success_url = reverse_lazy("publish:group:list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(PublishGroupCreateView, self).form_valid(form)