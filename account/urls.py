from django.urls import path, include
from account.views.sshpublickey import SSHPublicKeyListView, SSHPublicKeyCreateView


key_urlpattern = ([
    path("list", SSHPublicKeyListView.as_view(), name="list"),
    path("create", SSHPublicKeyCreateView.as_view(), name="create")
], "sshpublickey")

device_urlpattern = ([
    path("list", SSHPublicKeyListView.as_view(), name="list"),
    path("create", SSHPublicKeyCreateView.as_view(), name="create")
], "device")

urlpatterns = [
    path("sshpublickey/", include(key_urlpattern, namespace="sshpublickey"), name="sshpublickey_namespace"),
    path("device/", include(device_urlpattern, namespace="device"), name="device_namespace")
]