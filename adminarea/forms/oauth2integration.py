from django import forms
from django.forms import formset_factory
from django.contrib.auth import get_user_model, models
from publish.models import PublishGroup, PublishGroupToKeyGroup, OAuth2Integration
from account.models import KeyGroup, PublicKey, PublicKeyToKeyGroup
from sshock.contrib import get_master_user


class OAuth2IntegrationToPublishGroupForm(forms.Form):
  oauth2integration = forms.ModelMultipleChoiceField(required=False, queryset=OAuth2Integration.objects.none())