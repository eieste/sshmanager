from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class AccountDashboard(LoginRequiredMixin, TemplateView):
    """
        Dashboard after login
    """
    template_name = "account/dashboard.html"
