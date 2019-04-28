from django.urls import path
from . import views


urlpatterns = [
    path('sign_in/', views.sign_in),
    path('sign_up/', views.sign_up),
    path('', views.user_profile),
    path('sign_out/', views.sign_out),
    path('<int:id>', views.user_profile),


]
