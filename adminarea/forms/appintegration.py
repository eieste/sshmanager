from django import forms
from adminarea.models import AppIntegration, APP_INTEGRATIONS


class AppIntegrationForm(forms.ModelForm):

  class Meta:
    fields = ("platform", "display_name")
    model = AppIntegration

