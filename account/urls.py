from . import views
from django.urls import path
from .views import profile
from account.views import ChangePasswordView

urlpatterns = [
    path("home/",views.home, name='home'),
    path("signup/", views.signup, name='signup'),
    path("login/", views.loginpage, name='login'),
    path('logout', views.userlogout, name='logout'),
    path('profile/', profile, name='profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

]
