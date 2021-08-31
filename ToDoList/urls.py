from django.urls import path
from .views import delete_view, input_view, login_view, logout_view, signup_view, update_view

urlpatterns = [
    path('',input_view,name="home"),
    path('update/<int:key>/',update_view,name="update"),
    path('delete/<int:key>/',delete_view,name="delete"),
    path('signup/',signup_view,name="signup"),
    path('login/',login_view,name="login"),
    path('logout/',logout_view,name="logout"),
]
