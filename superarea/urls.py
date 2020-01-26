from django.urls import path, include
from superarea.views import *

app_name = "superarea"

publishgroup_urlpatterns = ([
    path("list", PublishGroupListView.as_view(), name="list"),
    path("create", PublishGroupCreateView.as_view(), name="create"),
    path("detail/<pk>", PublishGroupDetailView.as_view(), name="detail"),
    path("delete/<pk>", PublishGroupDeleteView.as_view(), name="delete")
], "publishgroup")


hostgroup_urlpatterns = ([
    path("list", HostGroupListView.as_view(), name="list"),
    path("create", HostGroupCreateView.as_view(), name="create"),
    path("delete", HostGroupDeleteView.as_view(), name="delete")
], "hostgroup")

host_urlpatterns = ([
    path("create", HostCreateView.as_view(), name="create"),
    path("delete/<pk>", HostDeleteView.as_view(), name="delete"),
    path("list", HostListView.as_view(), name="list")
], "host")


urlpatterns = [
    path("publishgroup/", include(publishgroup_urlpatterns, namespace="publishgroup")),
    path("hostgroup/", include(hostgroup_urlpatterns, namespace="hostgroup")),
    path("host/", include(host_urlpatterns, namespace="host")),
]