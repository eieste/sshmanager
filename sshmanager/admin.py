from django.contrib import admin
from sshmanager.models import Configuration
from sshmanager.forms import ConfigurationForm
# Register your models here.


def get_val(*args, **kwargs):
    return "bu"


class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ("key", "value", "description")
    form = ConfigurationForm
    list_editable = ("value",)
    change_list_form = ConfigurationForm

    def get_changelist_form(self, request, **kwargs):
        return ConfigurationForm


admin.site.register(Configuration, ConfigurationAdmin)
