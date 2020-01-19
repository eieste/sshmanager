from django.urls import path, include
from publish.views import PublishGroupListView, PublishGroupCreateView, \
    PublishGroupDetailView, PublishGroupDeleteView, OAuth2IntegrationListView,\
    OAuth2IntegrationCreateView, OAuth2IntegrationDeleteView, HostCreateView, HostListView


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
], "appintegration")

host_urlpatterns = ([
    path("create", HostCreateView.as_view(), name="create"),
    path("list", HostListView.as_view(), name="list")
], "host")


urlpatterns = [
    path('publishgroup/', include(publishgroup_urlpatterns, namespace="publishgroup")),
    path('appintegration/', include(oauth2integration_urlpatterns, namespace="appintegration")),
    path('host/', include(host_urlpatterns, namespace="host")),
]

