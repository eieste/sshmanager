from userarea.views import KeyGroupCreateView, KeyGroupUpdateView, KeyGroupDeleteView, KeyGroupListView
from django.urls import path, include
from userarea.views.device import DeviceCreateView, DeviceDeleteView, DeviceListView
from userarea.views.publickey import PublicKeyListView, PublicKeyCreateView, PublicKeyUpdateView, PublicKeyDeleteView
from django.urls import path, include

app_name = "userarea"

public_key_urlpattern = ([
    path("list", PublicKeyListView.as_view(), name="list"),
    path("create", PublicKeyCreateView.as_view(), name="create"),
    path("update/<pk>", PublicKeyUpdateView.as_view(), name="update"),
    path("delete/<pk>", PublicKeyDeleteView.as_view(), name="delete"),
], "publickey")

key_group_urlpattern = ([
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
    path("public-key/", include(public_key_urlpattern, namespace="public_key"), name="public_key"),
    path("key-group/", include(key_group_urlpattern, namespace="key_group")),
    path("device/", include(device_urlpattern, namespace="device"))
]