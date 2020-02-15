from django.contrib import messages
from django.views.generic import View
from django.http import HttpResponse
from sshock.contrib.views import JSONView
from django.contrib import messages
from django.utils.translation import pgettext

class ToastMessageJSView(JSONView):

    def get(self, request):
        json_data = []

        for msg in messages.get_messages(self.request):
            print(msg.__dict__)

            if msg.level == messages.DEBUG:
                msg_title = pgettext("Django Message Title", "DEBUG -- Message")
                msg_type = "info"
            elif msg.level == messages.INFO:
                msg_title = pgettext("Django Message Title", "Information")
                msg_type = "info"
            elif msg.level == messages.SUCCESS:
                msg_title = pgettext("Django Message Title", "Success")
                msg_type = "success"
            elif msg.level == messages.WARNING:
                msg_title = pgettext("Django Message Title", "Warning")
                msg_type = "warning"
            elif msg.level == messages.ERROR:
                msg_title = pgettext("Django Message Title", "Error")
                msg_type = "error"


            if messages.get_level(self.request) <= msg.level:
                json_data.append({
                    "title": msg_title,
                    "content": msg.message,
                    "type": msg_type
                })

        return self.render_to_response({
            "text": json_data
        })