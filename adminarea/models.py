import urllib.parse
import uuid

from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.db import models
from django.http import HttpResponseRedirect
from sshock.models import EntryMeta, VisibilityMeta

from superarea.models import PublishGroup

APP_INTEGRATIONS = [
    ("gitlab", "Gitlab"),
    ("github", "Github"),
    ("hetzner", "Hetzner"),
    ("ovh", "OVH"),
    ("scaleway", "Scaleway"),
    ("digitalocean", "Digital Ocean")
]


class AppIntegration(EntryMeta, VisibilityMeta, models.Model):
    platform = models.CharField(max_length=255, choices=APP_INTEGRATIONS)

    display_name = models.CharField(max_length=255)

    #: Token used for apis without OAuth2 Access
    token = models.CharField(max_length=255, blank=True, null=True)

    #: OAuth2 Credentials
    access_id = models.CharField(max_length=255, blank=True, null=True)
    secret_key = models.CharField(max_length=255, blank=True, null=True)

    #: Application URL / API Endpoint
    url = models.URLField(blank=True, null=True)

    global_visibility = models.BooleanField(default=False)
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


class AppIntegrationToPublishGroup(EntryMeta, models.Model):
    app_integration = models.ForeignKey(AppIntegration, on_delete=models.CASCADE)
    publish_group = models.ForeignKey(PublishGroup, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("app_integration", "publish_group")


class Organization(models.Model):
    display_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.pk}: {self.display_name}"