from django.contrib.auth import get_user_model
from django.conf import settings


def get_master_user():
    return get_user_model().objects.get(username=settings.MASTER_USERNAME)
