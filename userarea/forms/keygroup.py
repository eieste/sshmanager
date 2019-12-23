from django import forms

from superarea.models import PublishGroup
from userarea.models import KeyGroup


class KeyGroupCreateForm(forms.ModelForm):

    class Meta:
        fields = ("display_name",)
        model = KeyGroup

    def clean(self):
        self.cleaned_data['name'] = self.cleaned_data["display_name"]
        return self.cleaned_data


class AssignKeyGroupToPublicKeyForm(forms.Form):
    key_groups = forms.ModelMultipleChoiceField(queryset=KeyGroup.objects.none(), required=False)


class AssignPublishGroupToKeyGroupForm(forms.Form):
    template_form_name = "assign_publishgroup_to_keygroup_form"
    publish_groups = forms.ModelMultipleChoiceField(required=False, queryset=PublishGroup.objects.none())