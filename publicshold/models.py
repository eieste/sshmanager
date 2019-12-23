from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
import urllib.parse
from django.contrib.sites.shortcuts import get_current_site
import uuid
from django.conf import settings
from sshock.models import LinkedToMeta

OAUTH2_INTEGRATIONS = [
    ("gitlab", "Gitlab"),
    ("github", "Github")
]


class PublishGroup(LinkedToMeta, models.Model):
    name = models.SlugField(max_length=255)
    display_name = models.CharField(max_length=255)

    def __str__(self):
        return self.display_name


class UserToPublishGroup(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
    publish_group = models.ForeignKey(PublishGroup, on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="usertopublish_creator", on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ("user", "group", "publish_group")


class PublishGroupToKeyGroup(models.Model):
    publish_group = models.ForeignKey(PublishGroup, on_delete=models.CASCADE)
    key_group = models.ForeignKey("userarea.KeyGroup", on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    # aproved = models.BooleanField(default=False)

    class Meta:
        unique_together = ("publish_group", "key_group")
        permissions = (
            ("can_aprove_assignment", "Can confirm aprove"),
        )


class SSHPrivateKey(LinkedToMeta, models.Model):
    #: RFC 4716 formated SSH-Key
    ssh_private_key = models.TextField(max_length=2000)
    #: SHA256 Fingerprint of SSH-Key
    fingerprint = models.CharField(max_length=512)

    class Meta:
        unique_together = ('created_by', 'fingerprint',)
        permissions = (
            #: User can assign a device to created ssh public key
            ("can_assign_device", "Can Assign Device to SShPublicKey"),
        )


class HostGroup(LinkedToMeta, models.Model):
    display_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    private_key = models.ForeignKey(SSHPrivateKey, on_delete=models.DO_NOTHING)


class Host(LinkedToMeta, models.Model):
    host_group = models.ForeignKey(HostGroup, on_delete=models.CASCADE)
    host = models.CharField(max_length=255)
    user = models.CharField(max_length=255)


class HostToHostGroup(models.Model):
    host_server = models.ForeignKey(Host, on_delete=models.CASCADE)
    host_group = models.ForeignKey(HostGroup, on_delete=models.CASCADE)


class OAuth2Integration(models.Model):
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