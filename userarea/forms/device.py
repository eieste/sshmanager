from django import forms
from userarea.models import Device


class DeviceCreateForm(forms.ModelForm):

    class Meta:
        fields = ("display_name", "organizational_visibility", "global_visibility")
        model = Device

    def clean(self):
        self.cleaned_data['name'] = self.cleaned_data["display_name"]
        return self.cleaned_data
