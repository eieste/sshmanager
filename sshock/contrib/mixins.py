from django.http import JsonResponse
from django.utils.translation import pgettext
from partitialajax.mixin import CreatePartitialAjaxMixin
from django.urls import reverse_lazy


class JSONResponseMixin:
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return context


class PartitialFormMixin:
    partitial_form_url = "/"
    partitial_singleobject_form_url = None
    partitial_form_title = pgettext("Default Page title", "Create Everything")
    partitial_bundle_name = "app_modal_action"
    partitial_cancel_url = None
    template_name = "sshock/partitial/main.html"
    partitial_list = {
        ".modal-content": "sshock/partitial/partitial_form.html"
    }

    def get_partitial_list(self, *args, **kwargs):
        partitial_list = super().get_partitial_list(*args, **kwargs)
        partitial_list.update(self.partitial_list)
        return partitial_list

    def get_partitial_form_url(self):
        if self.partitial_singleobject_form_url is not None:
            return reverse_lazy(self.partitial_singleobject_form_url, kwargs={"pk": self.object.pk})
        return self.partitial_form_url

    def get_partitial_form_title(self):
        return self.partitial_form_title

    def get_partitial_bundle_name(self):
        return self.partitial_bundle_name

    def get_partitial_cancel_url(self):
        if self.partitial_cancel_url is not None:
            return self.partitial_cancel_url
        else:
            return self.success_url

    def get_context_data(self, **kwargs):
        kwargs["partitial_page"] = {
            "partitial_form_url": self.get_partitial_form_url(),
            "partitial_form_title": self.get_partitial_form_title(),
            "partitial_bundle_name": self.get_partitial_bundle_name(),
            "partitial_cancel_url": self.get_partitial_cancel_url()
        }
        ctx = super().get_context_data(**kwargs)
        return ctx

