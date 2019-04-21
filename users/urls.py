from django.urls import path
from . import views


urlpatterns = [
    path('sign_in/', views.sign_in),
    path('sign_up/', views.sign_up),
    path('^(?P<pk>\d+)', views.user_profile),
    path('', views.get_users),
    path('sign_out/', views.sign_out),



]
