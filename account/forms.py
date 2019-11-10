from django import forms
from account.models import SSHPublicKey
from Crypto.PublicKey import RSA
from account.models import Device, KeyGroup


class SSHPublicKeyCreateForm(forms.ModelForm):

    class Meta:
        fields = ("ssh_public_key", "device")
        model = SSHPublicKey

    def clean_key(self):
        key_string = self.cleaned_data.get("key")
        key = RSA.importKey(key_string)
        return key.export_key('PEM').decode("utf-8")


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
