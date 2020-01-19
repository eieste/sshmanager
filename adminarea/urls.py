from django.urls import path, include

from adminarea.views import AppIntegrationListView, \
    AppIntegrationCreateView, AppIntegrationDeleteView, AppIntegrationDetailView

app_name = "adminarea"

oauth2integration_urlpatterns = ([
    path("list", AppIntegrationListView.as_view(), name="list"),
    path("create", AppIntegrationCreateView.as_view(), name="create"),
    path("delete/<pk>", AppIntegrationDeleteView.as_view(), name="delete"),
    path("detail/<pk>", AppIntegrationDetailView.as_view(), name="detail"),
], "appintegration")

urlpatterns = [
    path('appintegration/', include(oauth2integration_urlpatterns, namespace="appintegration")),
]

