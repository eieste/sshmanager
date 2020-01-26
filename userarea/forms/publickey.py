from django import forms
from userarea.models import PublicKey
from Crypto.PublicKey import RSA
from userarea.models import KeyGroup
from superarea.models import PublishGroup
from django.utils.translation import pgettext as _
from django_ace import AceWidget


class PublicKeyCreateForm(forms.ModelForm):
    key_groups = forms.ModelMultipleChoiceField(queryset=KeyGroup.objects.none(), required=False)


    class Meta:
        fields = ("name", "ssh_public_key", "device")
        model = PublicKey

    def clean_ssh_public_key(self):
        try:
            ssh_public_key_string = self.cleaned_data.get("ssh_public_key", "")
            ssh_public_key = RSA.importKey(ssh_public_key_string)
            return ssh_public_key.export_key('PEM').decode("utf-8")
        except ValueError:
            raise forms.ValidationError(_("SSHPublicKeyCreateForm key input validation error (Invalid key)", "This is not a valid RSA Key"))
