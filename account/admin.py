from django.contrib import admin
from account.models import AccountUser, Device, SSHPublicKey, KeyGroup
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.html import format_html

# Register your models here.

class AccountUserAdmin(UserAdmin):


    def get_list_display(self, request):
        list_display = list(self.list_display)
        list_display.append("show_firm_url")
        return list_display


    def show_firm_url(self, obj):
        print(obj.pk)
        link = reverse('impersonate-start', args=[obj.id])

        #        link = reverse("impersonate-start", uid=obj.pk)
        return format_html("<a href='{url}'>Impersonate</a>", url=link)

    show_firm_url.allow_tags = True


admin.site.register(AccountUser, AccountUserAdmin)



class DeviceAdmin(admin.ModelAdmin):
    list_display = ("created_by", "name", "display_name")

admin.site.register(Device, DeviceAdmin)


class SSHPublicKeyAdmin(admin.ModelAdmin):
    list_display = ("created_by", "ssh_public_key", "fingerprint", "create_at", "device")

admin.site.register(SSHPublicKey, SSHPublicKeyAdmin)
admin.site.register(KeyGroup)
