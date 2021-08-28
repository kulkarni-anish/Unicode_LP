from django.urls import path
from .views import delete_view, input_view,update_view

urlpatterns = [
    path('',input_view,name="home"),
    path('update/<int:key>/',update_view,name="update"),
    path('delete/<int:key>/',delete_view,name="delete"),
]
