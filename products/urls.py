 #==================function best view ===================================


# from django.urls import path
# from . import views
#
# urlpatterns = [
#
#     path('',views.get_products),
#     path('add/',views.add_product),
#
# ]

 #==================class best view ===================================



from django.urls import path
from . import views

urlpatterns = [

    path('',views.GetProducts.as_view()),
    path('add/',views.AddProducts.as_view()),
    path('update/<int:pk>',views.UpdateProducts.as_view()),
]
