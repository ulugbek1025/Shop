from django.urls import path,include
from .views import index,detail

urlpatterns=[
    path('',index,name='home'),
    path('<int:id>/',detail,name='detail'),
]