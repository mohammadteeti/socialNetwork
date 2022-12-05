# dwitter/urls.py
from django.urls import path, include ,reverse_lazy
from .views import dashboard, profile_list, profile, register, myLogout
from django.views.generic.base import RedirectView
from django.contrib.auth import views as auth_views
from . import views
from social.settings import BASE_DIR
import os
app_name = "dwitter"

reg_templates_path =os.path.join( BASE_DIR ,"dwitter/templates")
print (reg_templates_path)
urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    # we can use RedirectView as a class-Based redirect
    path("dashboard/", RedirectView.as_view(url="/")),
    # we can create a specific view for the same purpose instead
    # path('dashboard/',goToDashboard.as_view()),
    
    #-----------------------auth and registrations url routing-----------------------------
    
    
    path("register/", register, name="register"),
    #path("accounts/", include("django.contrib.auth.urls")), 
    path('login/',auth_views.LoginView.as_view(template_name="registration/login.html"),name='login'),
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name=reg_templates_path+"/registration/password_change_form.html",success_url=reverse_lazy('dwitter:password_change_done')),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name=reg_templates_path+"/registration/password_change_done.html"),name='password_change_done'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name=reg_templates_path+"/registration/password_reset_form.html",success_url=reverse_lazy('dwitter:password_reset_done')),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name=reg_templates_path+"/registration/password_reset_done.html"),name='password_reset_done'),
    path('password_reset/confirm/',auth_views.PasswordResetConfirmView.as_view(template_name=reg_templates_path+"/registration/password_reset_confirm.html",success_url=reverse_lazy('dwitter:password_reset_complete')),name='password_reset_confirm'),

    path('logout/',auth_views.LogoutView.as_view(template_name="registration/logged_out.html"),name='logout'),
    
    #--------------------------------------------------------
    # just to customize logout page
    path("myLogout/", myLogout, name="myLogout"),
    # problem:
    # we have to define password_reset_done and password_change_done
    # views urls explicitly because we are using an app_name namespace attribute
    # and those templates doesn't use namespace in django
]
#
"""
path('dashboard/',RedirectView.as_view(url='/'))

in the above example redirect we can define a view in 
views.py as 
    
class goToDashboard(RedirectView):
url='/'
    
and then use this here in urls.py
path(' dashboard/ ',goToDashboard.as_view() )
    
this will result the same as the line above   
"""
#
