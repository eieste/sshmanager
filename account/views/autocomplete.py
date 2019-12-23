from django.views import View
from sshock.contrib.views import JSONView
from account.models import Device, KeyGroup
from sshock.contrib import get_master_user


class DevicesAutocompleteView(JSONView):

    def get_data(self, *args, **kwargs):
        """
        finds all devices containing the given string
        :return dict: list with all results of founded devices
        """
        queryset = Device.objects.filter(display_name__contains=self.request.GET.get("term", ""), created_by__in=[self.request.user, get_master_user()])
        return {
            "results": [ {"id": item.pk, "text": item.display_name} for item in queryset]
        }


class KeyGroupsAutocompleteView(JSONView):

    def get_data(self, *args, **kwargs):
        """
        finds all keygroups containing the given string
        :return dict: list with all results of founded keygroups
        """
        queryset = KeyGroup.objects.filter(display_name__contains=self.request.GET.get("term", ""), created_by__in=[self.request.user, get_master_user()], sshpublickeytokeygroup__isnull=True)
        return {
            "results": [ {"id": item.pk, "text": item.display_name} for item in queryset]
        }