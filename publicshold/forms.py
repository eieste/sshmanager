from django import forms
from django.forms import formset_factory
from django.contrib.auth import get_user_model, models
from publish.models import PublishGroup, PublishGroupToKeyGroup, OAuth2Integration
from account.models import KeyGroup, PublicKey, PublicKeyToKeyGroup
from sshock.contrib import get_master_user


class PublishGroupToKeyGroupForm(forms.Form):
  key_group = forms.MultipleChoiceField(
    widget=forms.CheckboxSelectMultiple,
  )

  def __init__(self, *args, **kwargs):
    user = kwargs.pop('user')
    object = kwargs.pop('object')
    super(PublishGroupToKeyGroupForm, self).__init__(*args, **kwargs)
    self.fields['key_group'].choices = [(item.pk, item.display_name) for item in KeyGroup.objects.filter(created_by__in=[get_master_user(), user])]


class UserToPublishGroupForm(forms.Form):
  users = forms.ModelMultipleChoiceField(required=False, queryset=get_user_model().objects.filter(is_active=True))
  groups = forms.ModelMultipleChoiceField(required=False, queryset=models.Group.objects.all())


class OAuth2IntegrationToPublishGroupForm(forms.Form):
  oauth2integration = forms.ModelMultipleChoiceField(required=False, queryset=OAuth2Integration.objects.none())