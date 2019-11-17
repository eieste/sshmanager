from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, FormView
from publish.models import PublishGroup, PublishGroupToKeyGroup, UserToPublishGroup
from account.models import KeyGroup
from django.urls import reverse_lazy
from publish.forms import PublishGroupToKeyGroupForm, UserToPublishGroupForm
from sshmanager.contrib import get_master_user
from django.forms import formset_factory
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class UserAssignExtension:

    def get_user_assign_form(self):
        args = ()
        if self.request.method == "POST":
            args = (self.request.POST,)
        # print(UserToPublishGroup.objects.all())

        print(UserToPublishGroup.objects.filter(publish_group=self.object).values_list("user", flat=True))

        form = UserToPublishGroupForm(*args, initial={
            "groups": UserToPublishGroup.objects.filter(publish_group=self.object).values_list("group", flat=True),
            "users": UserToPublishGroup.objects.filter(publish_group=self.object).values_list("user", flat=True),
        })

        if self.request.method == "POST":
            form.is_valid()
        return form

    def user_assign_form_valid(self, user_assign_form):
        users = user_assign_form.cleaned_data.get("users", [])
        groups = user_assign_form.cleaned_data.get("groups", [])

        for dbitem in self.object.usertopublishgroup_set.all():

            if dbitem.user is not None:
                if dbitem not in users:
                    dbitem.delete()
            elif dbitem.group is not None:
                if dbitem.group not in groups:
                    dbitem.delete()

        for user in users:
            UserToPublishGroup.objects.get_or_create(user=user, publish_group=self.object, group=None, defaults={"created_by": self.request.user})

        for group in groups:
            UserToPublishGroup.objects.get_or_create(group=group, publish_group=self.object, user=None, defaults={"created_by": self.request.user})


class PublishGroupDetailView(LoginRequiredMixin, DetailView, UserAssignExtension):
    template_name = "publish/publishgroup/publishgroup_detail.html"
    model = PublishGroup
    form_list = ["user_assign_form"]

    def get_context_data(self, **kwargs):
        ctx = super(PublishGroupDetailView, self).get_context_data(**kwargs)
        for formname in self.form_list:
            ctx[formname] = getattr(self, f"get_{formname}")()
        return ctx

    def post(self, *args, **kwargs):
        self.object = self.get_object()

        every_form_valid = True

        for formname in self.form_list:
            form = getattr(self, f"get_{formname}")()

            if form.is_valid():
                getattr(self, f"{formname}_valid")(form)
            else:
                every_form_valid = False

            if not every_form_valid:
                return self.get(*args, **kwargs)
        else:
            return redirect("publish:publishgroup:list")
