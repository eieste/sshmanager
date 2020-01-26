from django import forms
from adminarea.models import AppIntegrationToPublishGroup


class AppIntegrationToPublishGroupForm(forms.ModelForm):

    class Meta:
        model = AppIntegrationToPublishGroup
        fields = ("app_integration",)