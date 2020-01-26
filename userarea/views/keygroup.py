from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView, DetailView, DeleteView, ListView
from partitialajax.mixin import CreatePartitialAjaxMixin, ListPartitialAjaxMixin, DeletePartitialAjaxMixin, UpdatePartitialAjaxMixin, DetailPartitialAjaxMixin
from userarea.forms import KeyGroupCreateForm, AssignPublishGroupToKeyGroupForm
from userarea.models import KeyGroup
from superarea.models import PublishGroup, PublishGroupToKeyGroup
from django.http import HttpResponse
from sshock.contrib.mixins import PartitialFormMixin
from django.utils.translation import pgettext


class KeyGroupDeleteView(LoginRequiredMixin, PartitialFormMixin, DeletePartitialAjaxMixin, DeleteView):
    model = KeyGroup
    success_url = reverse_lazy("userarea:keygroup:list")
    partitial_form_url = reverse_lazy("userarea:keygroup:delete")
    partitial_bundle_name = "userarea_keygroup_delete"
    partitial_form_title = pgettext("Modal Title", "Delete Keygroup")
    partitial_cancel_url = reverse_lazy("userarea:keygroup:list")


class KeyGroupCreateView(LoginRequiredMixin, PartitialFormMixin, CreatePartitialAjaxMixin, CreateView):
    model = KeyGroup
    form_class = KeyGroupCreateForm
    success_url = reverse_lazy("userarea:keygroup:list")
    partitial_form_url = reverse_lazy("userarea:keygroup:create")
    partitial_bundle_name = "userarea_keygroup_delete"
    partitial_form_title = pgettext("Modal Title", "Create Keygroup")
    partitial_cancel_url = reverse_lazy("userarea:keygroup:list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.name = slugify(form.cleaned_data.get("display_name"))
        return super(KeyGroupCreateView, self).form_valid(form)


class KeyGroupUpdateView(LoginRequiredMixin, DetailPartitialAjaxMixin, DetailView):
    template_name = "userarea/keygroup/edit.html"
    model = KeyGroup
    partitial_list = {
        ".modal-content": "userarea/keygroup/partitial/edit.html"
    }

    def get_direct_context_data(self, *args, **kwargs):
        ctx = super().get_direct_context_data(*args, **kwargs)

        form = False
        if not self.request.method == "POST":
            form = AssignPublishGroupToKeyGroupForm(initial={})

        if "form" in kwargs:
            form = kwargs.pop("form")

        if form:
            form.fields["publish_groups"].queryset = PublishGroup.objects.filter(pk__in=self.request.user.usertopublishgroup_set.all().values_list("publish_group", flat=True))
            form.initial["publish_groups"] = PublishGroup.objects.filter(
                pk__in=self.request.user.publishgrouptokeygroup_set.all().values_list("publish_group", flat=True))
            ctx["key_group_form"] = form

        return ctx

    def ajax_get(self, *args, **kwargs):
        foo = super().ajax_get(*args, **kwargs)
        return foo

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

        return redirect(reverse_lazy("userarea:keygroup:detail", args=(self.object.pk,)))


class KeyGroupListView(LoginRequiredMixin, ListPartitialAjaxMixin, ListView):
    model = KeyGroup
    template_name = "userarea/keygroup/list.html"
    partitial_list = {
        "tbody#keygroup-list-partitial": "userarea/keygroup/partitial/list.html"
    }