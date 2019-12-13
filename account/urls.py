from django.urls import path, include
from account.views.sshpublickey import SSHPublicKeyListView, SSHPublicKeyCreateView, SSHPublicKeyDetailView, SSHPublicKeyDeleteView, AssignKeyGroupToSSHPublicKeyView, DissociateKeyGroupToSSHPublicKeyView
from account.views.device_and_keygroup import DeviceAndGroupListView, KeyGroupCreateView, KeyGroupDetailView, DeviceCreateView, KeyGroupDeleteView, DeviceDeleteView
from account.views.autocomplete import DevicesAutocompleteView, KeyGroupsAutocompleteView


app_name = "account"
sshpublickey_urlpattern = ([
    path("list", SSHPublicKeyListView.as_view(), name="list"),
    path("create", SSHPublicKeyCreateView.as_view(), name="create"),
    path("keygroup/assign/<pk>", AssignKeyGroupToSSHPublicKeyView.as_view(), name="keygroup-assign"),
    path("keygroup/dissociate/<pk>", DissociateKeyGroupToSSHPublicKeyView.as_view(), name="keygroup-dissociate"),
    path("detail/<pk>", SSHPublicKeyDetailView.as_view(), name="detail"),
    path("delete/<pk>", SSHPublicKeyDeleteView.as_view(), name="delete"),
], "sshpublickey")

device_urlpattern = ([
    path("create", DeviceCreateView.as_view(), name="create"),
    path("delete/<pk>/", DeviceDeleteView.as_view(), name="delete")
], "device")

keygroup_urlpattern = ([
    path("create", KeyGroupCreateView.as_view(), name="create"),
    path("detail/<pk>/", KeyGroupDetailView.as_view(), name="detail"),
    path("delete/<pk>/", KeyGroupDeleteView.as_view(), name="delete")
], "keygroup")

device_and_keygroup_urlpattern = ([
    path("list", DeviceAndGroupListView.as_view(), name="list"),
    path("device/", include(device_urlpattern, namespace="device")),
    path("publishgroup/", include(keygroup_urlpattern, namespace="publishgroup"))
], "device-and-keygroup")

urlpatterns = [
    path("sshpublickey/", include(sshpublickey_urlpattern, namespace="sshpublickey"), name="sshpublickey_namespace"),
    path("device-and-keygroup/", include(device_and_keygroup_urlpattern, namespace="device-and-keygroup")),
    path('avatar/', include('avatar.urls')),
    path("autocomplete/devices", DevicesAutocompleteView.as_view(), name="autocomplete_devices"),
    path("autocomplete/keygroups", KeyGroupsAutocompleteView.as_view(), name="autocomplete_devices")

]