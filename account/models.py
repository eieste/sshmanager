from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Account(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)


class Device(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.SlugField(max_length=255)
    display_name = models.CharField(max_length=255)


class KeyGroup(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.SlugField(max_length=255)
    display_name = models.CharField(max_length=255)


class SSHPublicKey(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    key = models.TextField(max_length=2000)
    fingerprint = models.CharField(max_length=512)
    create_at = models.DateTimeField(auto_now_add=True)
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('user', 'fingerprint',)


class SSHPublicKeyToKeyGroup(models.Model):
    ssh_public_key = models.ForeignKey("account.SSHPublicKey", on_delete=models.CASCADE)
    key_group = models.ForeignKey("account.KeyGroup", on_delete=models.CASCADE)