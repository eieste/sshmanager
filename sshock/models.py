from django.db import models
from django.conf import settings
from django.db.models import Q


DATATYPE_CHOICES = (
    (0, "string"),
    (1, "boolean"),
    (2, "number"),
    (3, "datetime"),
    (4, "option"),
)


class Configuration(models.Model):
    key = models.SlugField(max_length=255)
    datatype = models.PositiveSmallIntegerField(choices=DATATYPE_CHOICES)
    default = models.TextField()
    description = models.TextField()
    value = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.key}: {self.value}"


class LinkedToMeta(models.Model):
    """
        Add fields that allowes to define for which user this dataentry is
    """
    organization = models.ForeignKey("adminarea.Organization", on_delete=models.DO_NOTHING)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class VisibleToMeta(models.Model):
    """
        Add fields that descripes if the current entry is visible for all sshock users or is it only visible for all users at same organization
    """
    organizational_visibility = models.BooleanField(default=False)
    global_visibility = models.BooleanField(default=False)

    @classmethod
    def filter_by_visibility(cls, request):
        user = request.user
        return cls.objects.filter(Q(created_by=user) | Q(organizational_visibility=True, organization=user.organization) | Q(global_visibility=True) )

    class Meta:
        abstract = True