from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
import urllib.parse
from django.contrib.sites.shortcuts import get_current_site
from sshock.models import EntryMeta, VisibilityMeta
import uuid
from django.conf import settings


class PublishGroup(VisibilityMeta, EntryMeta, models.Model):
    name = models.SlugField(max_length=255)
    display_name = models.CharField(max_length=255)

    def __str__(self):
        return self.display_name


class UserToPublishGroup(EntryMeta, models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name="member")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
    publish_group = models.ForeignKey(PublishGroup, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "group", "publish_group")


class PublishGroupToKeyGroup(EntryMeta, models.Model):
    publish_group = models.ForeignKey(PublishGroup, on_delete=models.CASCADE)
    key_group = models.ForeignKey("userarea.KeyGroup", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("publish_group", "key_group")


class PrivateKey(EntryMeta, models.Model):
    #: Defines the key's affiliation to the user
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #: RFC 4716 formated SSH-Key
    ssh_private_key = models.TextField(max_length=2000)
    #: SHA256 Fingerprint of SSH-Key
    fingerprint = models.CharField(max_length=512)

    class Meta:
        unique_together = ('created_by', 'fingerprint',)


class HostGroup(EntryMeta, VisibilityMeta, models.Model):
    display_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    private_key = models.ForeignKey(PrivateKey, on_delete=models.DO_NOTHING)


class Host(EntryMeta, VisibilityMeta, models.Model):
    host_group = models.ForeignKey(HostGroup, on_delete=models.CASCADE)
    host = models.CharField(max_length=255)
    username = models.CharField(max_length=255)


class HostToHostGroup(EntryMeta, VisibilityMeta, models.Model):
    host_server = models.ForeignKey(Host, on_delete=models.CASCADE)
    host_group = models.ForeignKey(HostGroup, on_delete=models.CASCADE)
