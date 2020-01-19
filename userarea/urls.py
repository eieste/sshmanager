from userarea.views import KeyGroupCreateView, KeyGroupUpdateView, KeyGroupDeleteView, KeyGroupListView
from django.urls import path, include

from userarea.views.device import DeviceCreateView, DeviceDeleteView, DeviceListView
from userarea.views.publickey import PublicKeyListView, PublicKeyCreateView, PublicKeyDetailView, PublicKeyDeleteView
from django.urls import path, include

app_name = "userarea"

publickey_urlpattern = ([
    path("list", PublicKeyListView.as_view(), name="list"),
    path("create", PublicKeyCreateView.as_view(), name="create"),
    path("detail/<pk>", PublicKeyDetailView.as_view(), name="detail"),
    path("delete/<pk>", PublicKeyDeleteView.as_view(), name="delete"),
], "publickey")

keygroup_urlpattern = ([
    path("list", KeyGroupListView.as_view(), name="list"),
    path("create", KeyGroupCreateView.as_view(), name="create"),
    path("update/<pk>/", KeyGroupUpdateView.as_view(), name="update"),
    path("delete/<pk>/", KeyGroupDeleteView.as_view(), name="delete")
], "keygroup")

device_urlpattern = ([
    path("list", DeviceListView.as_view(), name="list"),
    path("create", DeviceCreateView.as_view(), name="create"),
    path("delete/<pk>/", DeviceDeleteView.as_view(), name="delete")
], "device")


urlpatterns = [
    path("publickey/", include(publickey_urlpattern, namespace="publickey"), name="publickey"),
    path("keygroup/", include(keygroup_urlpattern, namespace="keygroup")),
    path("device/", include(device_urlpattern, namespace="device"))
]