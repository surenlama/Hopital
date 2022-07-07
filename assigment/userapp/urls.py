from django.contrib import admin
from django.urls import path
from .views import Logout, SignUp,Signin,Dashboard


urlpatterns = [
    path('signup/', SignUp.as_view(), name="signup"),
    path('login/', Signin.as_view(), name='login'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('logout/', Logout.as_view(), name='logout'),

]
