from django.views.generic import CreateView
from account.models import KeyGroup
from account.forms import KeyGroupCreateForm
from django.urls import reverse_lazy


class KeyGroupCreateView(CreateView):
    template_name = "account/group/keygroup/keygroup_create.html"
    model = KeyGroup
    form_class = KeyGroupCreateForm
    success_url = reverse_lazy("device-and-keygroup:group:create")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(KeyGroupCreateView, self).form_valid(form)

