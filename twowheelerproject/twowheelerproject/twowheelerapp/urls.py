from.  import views
from django.urls import path,include

urlpatterns = [

    path('',views.home,name='home'),
    path('index',views.index,name='index')



    #path('add/',views.addition,name='addition')
]