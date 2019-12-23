from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from superarea.models import PublishGroup


class PublishGroupCreateView(LoginRequiredMixin, CreateView):
    template_name = "publish/../../templates/superarea/publishgroup/create.html"
    model = PublishGroup
    fields = ("display_name",)

    def get_success_url(self):
        return reverse_lazy("publish:publishgroup:detail", args=[self.object.pk])

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(PublishGroupCreateView, self).form_valid(form)


class PublishGroupListView(LoginRequiredMixin, ListView):
    template_name = "publish/../../templates/superarea/publishgroup/list.html"
    model = PublishGroup


class PublishGroupDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "publish/../../templates/superarea/publishgroup/delete.html"
    model = PublishGroup

    def get_success_url(self):
        return reverse_lazy("publish:publishgroup:list")


