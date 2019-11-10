from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class AccountDashboard(LoginRequiredMixin, TemplateView):
    template_name = "sshmanager/page.html"
