from django.contrib import admin
from account.models import Device, SSHPublicKey, KeyGroup
# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    list_display = ("created_by", "name", "display_name")

admin.site.register(Device, DeviceAdmin)


class SSHPublicKeyAdmin(admin.ModelAdmin):
    list_display = ("created_by", "ssh_public_key", "fingerprint", "create_at", "device")

admin.site.register(SSHPublicKey, SSHPublicKeyAdmin)
admin.site.register(KeyGroup)
