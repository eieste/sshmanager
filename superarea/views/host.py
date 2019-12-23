from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView

from superarea.models import Host


class HostCreateView(LoginRequiredMixin, CreateView):
    template_name = "superarea/host/create.html"
    model = Host


class HostListView(LoginRequiredMixin, ListView):
    template_name = "superarea/host/list.html"
    model = Host
    fields = ("")

    def get_queryset(self):
        return self.request.user.host_set.all()