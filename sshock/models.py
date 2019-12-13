from django.db import models


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
