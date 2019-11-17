from django.urls import path, include
from account.views.sshpublickey import SSHPublicKeyListView, SSHPublicKeyCreateView
from account.views.device_and_keygroup import DeviceAndGroupListView
from account.views.device import DeviceCreateView
from account.views.keygroup import KeyGroupCreateView, KeyGroupDetailView

app_name = "account"
sshpublickey_urlpattern = ([
    path("list", SSHPublicKeyListView.as_view(), name="list"),
    path("create", SSHPublicKeyCreateView.as_view(), name="create")
], "sshpublickey")

device_urlpattern = ([
    path("create", DeviceCreateView.as_view(), name="create")
], "device")

keygroup_urlpattern = ([
    path("create", KeyGroupCreateView.as_view(), name="create"),
    path("detail/<pk>/", KeyGroupDetailView.as_view(), name="detail")
], "keygroup")

device_and_keygroup_urlpattern = ([
    path("list", DeviceAndGroupListView.as_view(), name="list"),
    path("device/", include(device_urlpattern, namespace="device")),
    path("group/", include(keygroup_urlpattern, namespace="group"))
], "device-and-keygroup")

urlpatterns = [
    path("sshpublickey/", include(sshpublickey_urlpattern, namespace="sshpublickey"), name="sshpublickey_namespace"),
    path("device-and-keygroup/", include(device_and_keygroup_urlpattern, namespace="device-and-keygroup")),
    path('avatar/', include('avatar.urls')),

]