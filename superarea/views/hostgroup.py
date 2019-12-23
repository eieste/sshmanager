from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from superarea.models import HostGroup


class HostGroupCreateView(LoginRequiredMixin, ListView):
    template_name = "superarea/hostgroup/create.html"
    model = HostGroup

class HostGroupListView(LoginRequiredMixin, ListView):
    template_name = "superarea/hostgroup/list.html"
    model = HostGroup