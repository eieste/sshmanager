from django.views.generic import CreateView, DetailView
from account.models import KeyGroup
from publish.models import PublishGroup
from account.forms import KeyGroupCreateForm, AssignPublishGroupToKeyGroupForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class KeyGroupCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ["account.add_keygroup"]
    template_name = "account/device_and_keygroup/keygroup/keygroup_create.html"
    model = KeyGroup
    form_class = KeyGroupCreateForm
    success_url = reverse_lazy("device-and-keygroup:group:create")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(KeyGroupCreateView, self).form_valid(form)


class KeyGroupDetailView(LoginRequiredMixin, DetailView):
    template_name = "account/device_and_keygroup/keygroup/keygroup_detail.html"
    model = KeyGroup

    def get_context_data(self, **kwargs):
        ctx = super(KeyGroupDetailView, self).get_context_data(**kwargs)

        form = False
        if not self.request.method == "POST":
            form = AssignPublishGroupToKeyGroupForm(initial={})

        if "form" in kwargs:
            form = kwargs.pop("form")

        if form:
            form.fields["publish_groups"].queryset = PublishGroup.objects.filter(pk__in=self.request.user.usertopublishgroup_set.all().values_list("publish_group", flat=True))
            ctx["publish_group_form"] = form

        return ctx

    def post(self, *args, **kwargs):
        self.object = self.get_object()

        form = AssignPublishGroupToKeyGroupForm(self.request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            ctx = self.get_context_data(object=self.object, form=form)
            return self.render_to_response(ctx)


    def form_valid(self, form):
        pass