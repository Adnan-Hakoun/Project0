# from django.urls import path
# from . import views
#
# urlpatterns = [
#
#     path('',views.get_makers),
#     path('add/',views.add_maker),
#
# ]
 #==================class best view ===================================



from django.urls import path
from . import views

urlpatterns = [

    path('',views.GetMakers.as_view()),
    path('add/',views.AddMaker.as_view()),
]
