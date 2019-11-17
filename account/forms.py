from django import forms
from account.models import SSHPublicKey
from Crypto.PublicKey import RSA
from account.models import Device, KeyGroup, AccountUser
from publish.models import PublishGroup
from django.utils.translation import pgettext as _


class SSHPublicKeyCreateForm(forms.ModelForm):
    key_groups = forms.ModelMultipleChoiceField(queryset=KeyGroup.objects.none(), required=False)

    class Meta:
        fields = ("name", "ssh_public_key", "device")
        model = SSHPublicKey

    def clean_ssh_public_key(self):
        try:
            ssh_public_key_string = self.cleaned_data.get("ssh_public_key", "")
            ssh_public_key = RSA.importKey(ssh_public_key_string)
            return ssh_public_key.export_key('PEM').decode("utf-8")
        except ValueError:
            raise forms.ValidationError(_("SSHPublicKeyCreateForm key input validation error (Invalid key)", "This is not a valid RSA Key"))

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


class AssignKeyGroupToSSHPublicKeyForm(forms.Form):
    key_groups = forms.ModelMultipleChoiceField(queryset=KeyGroup.objects.none(), required=False)


class AssignPublishGroupToKeyGroupForm(forms.Form):
    template_form_name = "assign_publishgroup_to_keygroup_form"
    publish_groups = forms.ModelMultipleChoiceField(required=False, queryset=PublishGroup.objects.none())