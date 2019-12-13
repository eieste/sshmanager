from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView

from publish.models import Host


class HostCreateView(LoginRequiredMixin, CreateView):
    template_name = "publish/host/host_create.html"
    model = Host


class HostListView(LoginRequiredMixin, ListView):
    template_name = "publish/host/host_list.html"
    model = Host
    fields = ("")

    def get_queryset(self):
        return self.request.user.host_set.all()