from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from sshock.contrib import get_master_user
from adminarea.models import APP_INTEGRATIONS
from sshock.models import LinkedToMeta, VisibleToMeta


class OAuth2Account(models.Model):
    platform = models.CharField(choices=APP_INTEGRATIONS, max_length=255)
    code = models.CharField(max_length=255)


class Device(LinkedToMeta, VisibleToMeta, models.Model):
    """
        Create a Device entry.
        Each device can be assigned to multiple SSHPublic Keys.
    """
    #: Slugifey display_name (Used as comment at each publication)
    name = models.SlugField(max_length=255)
    #: Device name
    display_name = models.CharField(max_length=255)

    def __str__(self):
        return self.display_name

    class Meta:
        permissions = (
            ("self_manage", "Can create and delete Devices for itself "),
            ("organizational_manage", "Can create and delete Devices for the hole Organization"),
            ("global_manage", "Can create and delete Devices for the entire Apllication")
        )
        default_permissions = ()


class KeyGroup(models.Model):
    """
        Can be used to Group SSH-Keys by Projects
    """
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.SlugField(max_length=255)
    display_name = models.CharField(max_length=255)

    def __str__(self):
        return self.display_name

    def is_global(self):
        if self.created_by.pk is get_master_user().pk:
            return True
        return False


class PublicKey(models.Model):
    """
        Public Keys for publish to Server or Platforms
    """
    name = models.CharField(max_length=255)
    #: Defines the key's affiliation to the user
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #: RFC 4716 formated SSH-Key
    ssh_public_key = models.TextField(max_length=2000)
    #: SHA256 Fingerprint of SSH-Key
    fingerprint = models.CharField(max_length=512)
    create_at = models.DateTimeField(auto_now_add=True)
    #: defines on which device the SSH-Key was generated
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('created_by', 'fingerprint',)
        permissions = (
            #: User can assign a device to created ssh public key
            ("can_assign_device", "Can Assign Device to SShPublicKey"),
        )


class PublicKeyToKeyGroup(models.Model):
    public_key = models.ForeignKey("userarea.PublicKey", on_delete=models.CASCADE)
    key_group = models.ForeignKey("userarea.KeyGroup", on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ("public_key", "key_group")