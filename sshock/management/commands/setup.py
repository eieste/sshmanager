from django.core.management.base import BaseCommand, CommandError
import logging
from django.utils import timezone
from adminarea.models import Organization
from django.utils.translation import gettext, gettext_lazy as _

log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Setup SSH-Manager'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        log.info("Create Default Organization")
        Organization.objects.create(name="default", created_by=1, created_at=timezone.now(), display_name="Default Organization")
