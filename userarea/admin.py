from django.contrib import admin

from userarea.models import PublicKey, KeyGroup, Device


# Register your models here.
class PublicKeyAdmin(admin.ModelAdmin):
    list_display = ("created_by", "ssh_public_key", "fingerprint", "create_at", "device")

admin.site.register(PublicKey, PublicKeyAdmin)


class KeyGroupAdmin(admin.ModelAdmin):
    list_display = ("created_by", "display_name", "name")
    fields = ("display_name", )

admin.site.register(KeyGroup, KeyGroupAdmin)


class DeviceAdmin(admin.ModelAdmin):
    list_display = ("created_by", "display_name")


admin.site.register(Device, DeviceAdmin)