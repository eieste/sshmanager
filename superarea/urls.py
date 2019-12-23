from django.urls import path, include
from superarea.views import PublishGroupListView, HostGroupListView

app_name = "superarea"

publishgroup_urlpatterns = ([
    path("list", PublishGroupListView.as_view(), name="list")
], "publishgroup")


hostgroup_urlpatterns = ([
    path("list", HostGroupListView.as_view(), name="list")
], "hostgroup")


urlpatterns = [
    path("publishgroup/", include(publishgroup_urlpatterns, namespace="publishgroup")),
    path("hostgroup/", include(hostgroup_urlpatterns, namespace="superarea"))
]