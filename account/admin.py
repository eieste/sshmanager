from django.contrib import admin
from account.models import Device, SSHPublicKey
# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    list_display = ("user","name", "display_name")

admin.site.register(Device, DeviceAdmin)


class SSHPublicKeyAdmin(admin.ModelAdmin):
    list_display = ("user", "key", "fingerprint", "create_at", "device")

admin.site.register(SSHPublicKey, SSHPublicKeyAdmin)