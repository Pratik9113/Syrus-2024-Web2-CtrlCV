"""pratikwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from accounts.views import loginPage,registerPage
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accounts.views import activate_email
# from .views import home
# from .views import home
# from pratikwebsite import views
urlpatterns = [
    # path('home/index.html/', home, name='home'),
    path('login/',loginPage, name = "login"),
    path('register/',registerPage, name = "register"),
    # path('register/', registerPage, name="register_with_slash"),
    path('activate/<email_token>/' , activate_email , name="activate_email")
]