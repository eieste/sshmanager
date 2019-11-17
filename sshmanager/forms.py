from django import forms
from django.contrib.admin import widgets
from django.utils import timezone
import datetime

format = '%Y-%m-%dT%H:%M:%S%z'


class ConfigurationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ConfigurationForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance')


        if instance:
            initial_value = instance.value
            if instance.datatype is 0:
                self.fields['value'].widget = forms.TextInput()

            if instance.datatype is 1:
                self.fields['value'].widget = forms.CheckboxInput()
                if str(initial_value).lower() in ["t", "true", "y", "yes", "wahr", "w", "j", "ja"]:
                    initial_value = True
                else:
                    initial_value = False

            if instance.datatype is 2:
                self.fields['value'].widget = forms.NumberInput()

            if instance.datatype is 3:
                self.fields['value'].widget = widgets.AdminSplitDateTime()
                try:
                    initial_value = datetime.datetime.fromisoformat(instance.value)
                except ValueError as e:
                    initial_value = timezone.now()

            if instance.datatype is 4:
                options = instance.default.split(";")

                option_list = [ (item, item) for item in options]

                self.fields['value'].widget = forms.Select(choices=option_list)


            self.initial["value"] = initial_value

    def clean_value(self, *args, **kwargs):
        instance = self.instance
        value = self.cleaned_data.get("value")

        if instance.datatype is 3:
            dvalue = datetime.datetime.strptime(value, "['%d.%m.%Y', '%H:%M:%S']")
            return dvalue.isoformat()

        if instance.datatype is 1:
            print(str(value).lower())
            if str(value).lower() in ["t", "1", "true", "y", "yes", "wahr", "w", "j", "ja"]:
                return "yes"
            return "no"
        return value