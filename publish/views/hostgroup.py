from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from publish.models import HostGroup


class HostGroupCreateView(LoginRequiredMixin, ListView):
    template_name = "publish/hostgroup/hostgroup_create.html"
    model = HostGroup
