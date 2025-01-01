from django.urls import path
from . import views

from django.urls import path
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('', views.home, name='home'),
    path('no/', views.no_view, name='no'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile')

]
