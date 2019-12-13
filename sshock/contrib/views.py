from django.views.generic import TemplateView
from sshock.contrib.mixins import JSONResponseMixin


class JSONView(JSONResponseMixin, TemplateView):
    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)