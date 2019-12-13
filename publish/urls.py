from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from account.views.login import LoginView
from account.views.dashboard import AccountDashboard
from publish.views import PublishGroupListView, PublishGroupCreateView, \
    PublishGroupDetailView, PublishGroupDeleteView, OAuth2IntegrationListView,\
    OAuth2IntegrationCreateView, OAuth2IntegrationDeleteView, HostGroupCreateView, HostCreateView, HostListView


app_name = "publish"

publishgroup_urlpatterns = ([
    path("list", PublishGroupListView.as_view(), name="list"),
    path("detail/<int:pk>", PublishGroupDetailView.as_view(), name="detail"),
    path("delete/<pk>", PublishGroupDeleteView.as_view(), name="delete"),
    path("create", PublishGroupCreateView.as_view(), name="create")
], "publishgroup")

oauth2integration_urlpatterns = ([
    path("list", OAuth2IntegrationListView.as_view(), name="list"),
    path("create", OAuth2IntegrationCreateView.as_view(), name="create"),
    path("delete/<pk>", OAuth2IntegrationDeleteView.as_view(), name="delete"),
], "oauth2integration")

host_urlpatterns = ([
    path("create", HostCreateView.as_view(), name="create"),
    path("list", HostListView.as_view(), name="list")
], "host")


urlpatterns = [
    path('publishgroup/', include(publishgroup_urlpatterns, namespace="publishgroup")),
    path('oauth2integration/', include(oauth2integration_urlpatterns, namespace="oauth2integration")),
    path('host/', include(host_urlpatterns, namespace="host")),
]

