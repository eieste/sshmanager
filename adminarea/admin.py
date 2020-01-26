from django.contrib import admin
from adminarea.models import Organization
from django.utils.text import slugify


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("display_name", "name")
    fields = ("display_name",)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.name = slugify(form.cleaned_data.get("display_name"))
        super().save_model(request, obj, form, change)


admin.site.register(Organization, OrganizationAdmin)
