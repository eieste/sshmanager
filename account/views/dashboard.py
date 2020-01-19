from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from partitialajax.mixin import PartitialAjaxMixin


class AccountDashboard(LoginRequiredMixin, PartitialAjaxMixin, TemplateView):
    """
        Dashboard after login
    """
    template_name = "account/dashboard.html"
    partitial_list = {
        "#count-sshkey-dashboard": "sshock/pages/foobar.html",
        "#testpart": "sshock/pages/foobar.html"
    }
