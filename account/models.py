from django.db import models
from django.contrib.auth import get_user_model
from sshmanager.contrib import get_master_user

# Create your models here.


class Account(models.Model):
    """
        Additional Account Informations
    """
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)


class Device(models.Model):
    """
        Create a Device entry.
        Each device can be assigned to multiple SSHPublic Keys.
    """
    #: If user is settings.MASTER_USER the device was visible to all Users. if user is defined to specific user the device is only visible to than
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    #: Slugifey display_name (Used as comment at each publication)
    name = models.SlugField(max_length=255)
    #: Device name
    display_name = models.CharField(max_length=255)

    def __str__(self):
        return self.display_name

    def is_global(self):
        if self.user.pk is get_master_user().pk:
            return True
        return False


class KeyGroup(models.Model):
    """
        Can be used to Group SSH-Keys by Projects
    """
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.SlugField(max_length=255)
    display_name = models.CharField(max_length=255)

    def __str__(self):
        return self.display_name

    def is_global(self):
        if self.user.pk is get_master_user().pk:
            return True
        return False


class SSHPublicKey(models.Model):
    """
        Public Keys for publish to Server or Platforms
    """
    #: Defines the key's affiliation to the user
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    #: RFC 4716 formated SSH-Key
    ssh_public_key = models.TextField(max_length=2000)
    #: SHA256 Fingerprint of SSH-Key
    fingerprint = models.CharField(max_length=512)
    create_at = models.DateTimeField(auto_now_add=True)
    #: defines on which device the SSH-Key was generated
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('user', 'fingerprint',)


class SSHPublicKeyToKeyGroup(models.Model):
    ssh_public_key = models.ForeignKey("account.SSHPublicKey", on_delete=models.CASCADE)
    key_group = models.ForeignKey("account.KeyGroup", on_delete=models.CASCADE)
    aproved = models.BooleanField(default=False)