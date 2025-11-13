from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_entry, name='add_entry'),
    path('signup/', views.signup, name='signup'),  # signup route
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
