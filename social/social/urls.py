"""social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# social/urls.py
from django.contrib import admin
from django.urls import path, include,reverse_lazy
from django.contrib.auth import views as auth_views
from dwitter.urls import reg_templates_path
urlpatterns = [

path("", include("dwitter.urls",namespace='dwitter')),
path("admin/", admin.site.urls),
path("password_reset_confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name=reg_templates_path+"/registration/password_reset_confirm.html"),name="password_reset_confirm"),
path("password_reset_complete/",auth_views.PasswordResetCompleteView.as_view(template_name=reg_templates_path+"/registration/password_reset_complete.html"),name="password_reset_complete"),

]