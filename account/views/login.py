from django.contrib.auth import views
#from myapp.forms import UserLoginForm


class LoginView(views.LoginView):
    template_name = "account/accounting/login.html"
