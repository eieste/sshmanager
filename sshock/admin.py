from django.contrib import admin
from sshock.models import Configuration
from sshock.forms import ConfigurationForm
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ("key", "value", "description")
    form = ConfigurationForm
    list_editable = ("value",)
    change_list_form = ConfigurationForm

    def get_changelist_form(self, request, **kwargs):
        return ConfigurationForm


admin.site.register(Configuration, ConfigurationAdmin)


admin.site.site_title = ugettext_lazy('SSHock Admin')
admin.site.site_header = ugettext_lazy('SSHock Admin')
admin.site.index_title = ugettext_lazy('SSHock Admin')
