from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# Create your models here.
class Server(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    hostname = models.CharField(max_length=255)
    port = models.PositiveIntegerField()
    #key_group = models.ForeignKey


class ServerUser(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    host = models.ForeignKey(Server, on_delete=models.CASCADE)
    ssh_public_key = models.ForeignKey("account.SSHPublicKey", on_delete=models.CASCADE)
    username = models.CharField(max_length=255)


class ServerGroup(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.SlugField(max_length=255)
    display_name = models.CharField(max_length=255)


class ServerToServerGroup(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    server_group = models.ForeignKey(ServerGroup, on_delete=models.CASCADE)