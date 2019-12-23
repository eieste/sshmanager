from django.urls import path, include


app_name = "account"

urlpatterns = [
    path('avatar/', include('avatar.urls')),

]