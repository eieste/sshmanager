from django.contrib import admin
from django.utils.text import slugify
from userarea.models import PublicKey, KeyGroup, Device, PublicKeyToKeyGroup


# Register your models here.
class PublicKeyAdmin(admin.ModelAdmin):
    list_display = ("created_by", "ssh_public_key", "fingerprint", "created_at", "device")


admin.site.register(PublicKey, PublicKeyAdmin)


class PublicKeyToKeyGroupAdmin(admin.ModelAdmin):
    list_display = ("key_group","public_key")


admin.site.register(PublicKeyToKeyGroup, PublicKeyToKeyGroupAdmin)


class KeyGroupAdmin(admin.ModelAdmin):
    list_display = ("created_by", "display_name", "name")
    fields = ("display_name", )


admin.site.register(KeyGroup, KeyGroupAdmin)


class DeviceAdmin(admin.ModelAdmin):
    list_display = ("display_name", "created_by", "organization")
    fields = ("display_name", "organization", "organizational_visibility", "global_visibility")

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.name = slugify(form.cleaned_data.get("display_name"))
        super().save_model(request, obj, form, change)


admin.site.register(Device, DeviceAdmin)
