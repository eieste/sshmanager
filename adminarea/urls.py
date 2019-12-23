from django.urls import path, include

from adminarea.views import OAuth2IntegrationListView, \
    OAuth2IntegrationCreateView, OAuth2IntegrationDeleteView

app_name = "adminarea"

oauth2integration_urlpatterns = ([
    path("list", OAuth2IntegrationListView.as_view(), name="list"),
    path("create", OAuth2IntegrationCreateView.as_view(), name="create"),
    path("delete/<pk>", OAuth2IntegrationDeleteView.as_view(), name="delete"),
], "oauth2integration")

urlpatterns = [
    path('oauth2integration/', include(oauth2integration_urlpatterns, namespace="oauth2integration")),
]

