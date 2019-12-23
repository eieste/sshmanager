from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
import urllib.parse
from django.contrib.sites.shortcuts import get_current_site
import uuid
from django.conf import settings


class PublishGroup(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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


class PrivateKey(models.Model):
    #: Defines the key's affiliation to the user
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #: RFC 4716 formated SSH-Key
    ssh_private_key = models.TextField(max_length=2000)
    #: SHA256 Fingerprint of SSH-Key
    fingerprint = models.CharField(max_length=512)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('created_by', 'fingerprint',)
        permissions = (
            #: User can assign a device to created ssh public key
            ("can_assign_device", "Can Assign Device to SShPublicKey"),
        )


class HostGroup(models.Model):
    display_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    private_key = models.ForeignKey(PrivateKey, on_delete=models.DO_NOTHING)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)


class Host(models.Model):
    host_group = models.ForeignKey(HostGroup, on_delete=models.CASCADE)
    host = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)


class HostToHostGroup(models.Model):
    host_server = models.ForeignKey(Host, on_delete=models.CASCADE)
    host_group = models.ForeignKey(HostGroup, on_delete=models.CASCADE)
