from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from adminarea.models import OAuth2Integration


class OAuth2IntegrationListView(LoginRequiredMixin, ListView):
    template_name = "publish/../../templates/adminarea/oauth2integration/oauth2integration_list.html"
    model = OAuth2Integration


class OAuth2IntegrationCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = "publish/../../templates/adminarea/oauth2integration/oauth2integration_create.html"
    model = OAuth2Integration
    permission_required = ("publish.add_oauth2integration",)
    fields = ("platform", "display_name", "access_id", "secret_key", "url")

    def get_success_url(self):
        return reverse_lazy("publish:oauth2integration:list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(OAuth2IntegrationCreateView, self).form_valid(form)


class OAuth2IntegrationDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "publish/../../templates/adminarea/oauth2integration/oauth2integration_delete.html"
    model = OAuth2Integration

    def get_success_url(self):
        return reverse_lazy("publish:oauth2integration:list")