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


# Create your views here.


class PublishGroupListView(LoginRequiredMixin, ListView):
    template_name = "publish/group/list.html"
    model = PublishGroup

