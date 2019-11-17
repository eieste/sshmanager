from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView

from account.forms import KeyGroupCreateForm, AssignPublishGroupToKeyGroupForm
from account.models import KeyGroup
from publish.models import PublishGroup, PublishGroupToKeyGroup
from django.shortcuts import redirect
from django.urls import reverse_lazy


class KeyGroupDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = "account/device_and_keygroup/keygroup/keygroup_delete.html"
    model = KeyGroup
    permission_required = ["account.delete_keygroup"]
    success_url = reverse_lazy("account:device-and-keygroup:list")


class KeyGroupCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ["account.add_keygroup"]
    template_name = "account/device_and_keygroup/keygroup/keygroup_create.html"
    model = KeyGroup
    form_class = KeyGroupCreateForm
    success_url = reverse_lazy("account:device-and-keygroup:list")

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
            form.initial["publish_groups"] = PublishGroup.objects.filter(
            pk__in=self.request.user.publishgrouptokeygroup_set.all().values_list("publish_group", flat=True))
            ctx["publish_group_form"] = form

        return ctx

    def post(self, *args, **kwargs):
        self.object = self.get_object()

        form = AssignPublishGroupToKeyGroupForm(self.request.POST)
        form.fields["publish_groups"].queryset = PublishGroup.objects.filter(
            pk__in=self.request.user.usertopublishgroup_set.all().values_list("publish_group", flat=True))

        if form.is_valid():
            return self.form_valid(form)
        else:
            ctx = self.get_context_data(object=self.object, form=form)
            return self.render_to_response(ctx)

    def form_valid(self, form):
        publish_groups = form.cleaned_data.get("publish_groups", [])

        for dbitem in self.object.publishgrouptokeygroup_set.all():
            if dbitem not in publish_groups:
                dbitem.delete()

        for publish_group in publish_groups:
            PublishGroupToKeyGroup.objects.get_or_create(publish_group=publish_group, key_group=self.object, created_by=self.request.user)

        return redirect(reverse_lazy("account:device-and-keygroup:keygroup:detail", args=(self.object.pk,)))