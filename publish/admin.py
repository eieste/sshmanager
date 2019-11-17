from django.contrib import admin
from publish.models import *

# Register your models here.
class Oauth2IntegrationAdmin(admin.ModelAdmin):
    pass


admin.site.register(OAuth2Integration, Oauth2IntegrationAdmin)
admin.site.register(UserToPublishGroup)
admin.site.register(PublishGroup)