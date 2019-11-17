from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from account.views.login import LoginView
from account.views.dashboard import AccountDashboard
from publish.views import PublishGroupListView, PublishGroupCreateView, PublishGroupDetailView, PublishGroupDeleteView

app_name = "publish"

group_urlpatterns = ([
    path("list", PublishGroupListView.as_view(), name="list"),
    path("detail/<int:pk>", PublishGroupDetailView.as_view(), name="detail"),
    path("delete/<pk>", PublishGroupDeleteView.as_view(), name="delete"),
    path("create", PublishGroupCreateView.as_view(), name="create")
], "publishgroup")

urlpatterns = [
    path('publishgroup/', include(group_urlpatterns, namespace="publishgroup")),
]

