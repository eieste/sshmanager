from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from sshock.contrib import get_master_user
from publish.models import OAUTH2_INTEGRATIONS


class AccountUser(AbstractUser):

    def display_user(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return f"{self.first_name}"
        elif self.username:
            return f"{self.username}"
        return f"{self.email}"


class OAuth2Account(models.Model):
    platform = models.CharField(choices=OAUTH2_INTEGRATIONS, max_length=255)
    code = models.CharField(max_length=255)


class Device(models.Model):
    """
        Create a Device entry.
        Each device can be assigned to multiple SSHPublic Keys.
    """
    #: If user is settings.MASTER_USER the device was visible to all Users. if user is defined to specific user the device is only visible to than
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #: Slugifey display_name (Used as comment at each publication)
    name = models.SlugField(max_length=255)
    #: Device name
    display_name = models.CharField(max_length=255)

    def __str__(self):
        return self.display_name

    def is_global(self):
        if self.created_by.pk is get_master_user().pk:
            return True
        return False


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


class SSHPublicKey(models.Model):
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


class SSHPublicKeyToKeyGroup(models.Model):
    ssh_public_key = models.ForeignKey("account.SSHPublicKey", on_delete=models.CASCADE)
    key_group = models.ForeignKey("account.KeyGroup", on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ("ssh_public_key", "key_group")