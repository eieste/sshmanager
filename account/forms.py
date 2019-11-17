from django import forms
from account.models import SSHPublicKey
from Crypto.PublicKey import RSA
from account.models import Device, KeyGroup
from publish.models import PublishGroup


class SSHPublicKeyCreateForm(forms.ModelForm):

    class Meta:
        fields = ("ssh_public_key", "device")
        model = SSHPublicKey

    def clean_key(self):
        ssh_public_key_string = self.cleaned_data.get("key")
        ssh_public_key = RSA.importKey(ssh_public_key_string)
        return ssh_public_key.export_key('PEM').decode("utf-8")


class DeviceCreateForm(forms.ModelForm):

    class Meta:
        fields = ("display_name",)
        model = Device

    def clean(self):
        self.cleaned_data['name'] = self.cleaned_data["display_name"]
        return self.cleaned_data


class KeyGroupCreateForm(forms.ModelForm):

    class Meta:
        fields = ("display_name",)
        model = KeyGroup

    def clean(self):
        self.cleaned_data['name'] = self.cleaned_data["display_name"]
        return self.cleaned_data


class AssignPublishGroupToKeyGroupForm(forms.Form):
  publish_groups = forms.ModelMultipleChoiceField(required=False, queryset=PublishGroup.objects.none())