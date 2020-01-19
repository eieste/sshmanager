"""sshock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from account.views.login import LoginView
from account.views.dashboard import AccountDashboard
from django.views.i18n import JavaScriptCatalog
from django.http import HttpResponse, HttpResponseRedirect
import json
import urllib.parse
import requests

#
# def get_authorization(request):
#     git = OAuth2Integration.objects.first()
#
#     q = urllib.parse.parse_qs(request.META["QUERY_STRING"])
#
#     ra = requests.post("{}/oauth/token".format(git.url), {
#         "client_id": git.access_id,
#         "client_secret": git.secret_key,
#         "code": q["code"],
#         "grant_type": "authorization_code",
#         "redirect_uri": "http://localhost:8000/oauth/redirect"
#     })
#
#     access_token = ra.json()["access_token"]
#     return HttpResponse(ra.text, content_type="application/json; charset=utf-8")
#
#
# def auth_user(request):
#     git = OAuth2Integration.objects.first()
#     return git.authorize_user()
#
#     q = urllib.parse.urlencode({
#         "client_id": git.access_id,
#         "redirect_uri": "http://localhost:8000/oauth/redirect",
#         "response_type": "code",
#         "state": "UNIQUE_HASH",
#         "scope": ""
#     })
#     # https://gitlab.example.com/oauth/authorize?client_id=APP_ID&redirect_uri=REDIRECT_URI&response_type=token&state=YOUR_UNIQUE_STATE_HASH&scope=REQUESTED_SCOPES
#     return HttpResponseRedirect("{}/oauth/authorize?{}".format(git.url, q))
#
#
# def authorizeuser_view(requests, *args, **kwargs):
#     oauth_app = OAuth2Integration.objects.get("")
#     pass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view()),
    path('account/', include("account.urls")),
    path('super/', include("superarea.urls", namespace="superarea")),
    path('manage/', include("adminarea.urls", namespace="adminarea")),
    path('user/', include("userarea.urls", namespace="userarea")),
    path('', AccountDashboard.as_view(), name="account_dashboard"),
    path('impersonate/', include('impersonate.urls')),
    path('i18n/', JavaScriptCatalog.as_view(), name="javascript_catalog")
    #path("oauth/authorize", authorizeuser_view, name="oauth_authorizeuser"),
    #path('oauth/redirect', get_authorization),
    #path('oauth', auth_user)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
