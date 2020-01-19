from django.contrib.auth.models import AbstractUser
from django.db import models

from adminarea.models import APP_INTEGRATIONS


class AccountUser(AbstractUser):
    organization = models.ForeignKey("adminarea.Organization", on_delete=models.CASCADE, blank=True, null=True)

    def display_user(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return f"{self.first_name}"
        elif self.username:
            return f"{self.username}"
        return f"{self.email}"


class OAuth2Account(models.Model):
    platform = models.CharField(choices=APP_INTEGRATIONS, max_length=255)
    code = models.CharField(max_length=255)
