from django import forms
from account.models import SSHPublicKey
from Crypto.PublicKey import RSA


class SSHPublicKeyCreateForm(forms.ModelForm):

    class Meta:
        fields = ("key", "device")
        model = SSHPublicKey

    def clean_key(self):
        key_string = self.cleaned_data.get("key")
        key = RSA.importKey(key_string)
        return key.export_key('PEM').decode("utf-8")
