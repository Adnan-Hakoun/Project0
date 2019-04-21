from django.urls import path
from . import views

urlpatterns = [

    path('',views.get_products),
    path('add/',views.add_product),

]
