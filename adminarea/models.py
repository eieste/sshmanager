import urllib.parse
import uuid

from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.db import models
from django.http import HttpResponseRedirect
from sshock.models import LinkedToMeta

from superarea.models import PublishGroup

OAUTH2_INTEGRATIONS = [
    ("gitlab", "Gitlab"),
    ("github", "Github")
]


class OAuth2Integration(LinkedToMeta, models.Model):
    platform = models.CharField(max_length=255, choices=OAUTH2_INTEGRATIONS)

    display_name = models.CharField(max_length=255)

    access_id = models.CharField(max_length=255)
    secret_key = models.CharField(max_length=255)

    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    active = models.BooleanField(default=True)

    def __str__(self):
        return f"[{self.get_platform_display()}] {self.display_name}"

    def authorize_user(self, request):

        if self.platform is "gitlab":
            return self.authorize_user_by_gitlab(request)
        if self.platform is "github":
            return self.authorize_user_by_github(request)

    def authorize_user_by_gitlab(self, request):
        state = uuid.uuid4().hex
        q = urllib.parse.urlencode({
            "client_id": self.access_id,
            "redirect_uri": f"{get_current_site()}/oauth/redirect",
            "response_type": "code",
            "state": state,
            "scope": "api"
        })
        request.session["oauth_sate"] = state
        return HttpResponseRedirect(f"{self.url}/oauth/authorize?{q}")

    def authorize_user_by_github(self, request):
        pass


class OAuth2IntegrationToPublishGroup(models.Model):
    oauth2_integration = models.ForeignKey(OAuth2Integration, on_delete=models.CASCADE)
    publish_group = models.ForeignKey(PublishGroup, on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ("oauth2_integration", "publish_group")


class Organization(models.Model):
    display_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255, unique=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_by")
    created_at = models.DateTimeField(auto_now_add=True)