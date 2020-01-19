from django.urls import path, include
from superarea.views import PublishGroupListView, HostGroupListView, PublishGroupCreateView, PublishGroupDeleteView, PublishGroupDetailView

app_name = "superarea"

publishgroup_urlpatterns = ([
    path("list", PublishGroupListView.as_view(), name="list"),
    path("create", PublishGroupCreateView.as_view(), name="create"),
    path("detail/<pk>", PublishGroupDetailView.as_view(), name="detail"),
    path("delete/<pk>", PublishGroupDeleteView.as_view(), name="delete")
], "publishgroup")


hostgroup_urlpatterns = ([
    path("list", HostGroupListView.as_view(), name="list")
], "hostgroup")


urlpatterns = [
    path("publishgroup/", include(publishgroup_urlpatterns, namespace="publishgroup")),
    path("hostgroup/", include(hostgroup_urlpatterns, namespace="superarea"))
]