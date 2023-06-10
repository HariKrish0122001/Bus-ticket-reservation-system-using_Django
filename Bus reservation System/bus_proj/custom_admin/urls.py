from django.urls import path,include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.admin_login,name="admin_login"),
    path('sign_in',views.admin_signin,name="sign_in"),
    path('dashboard',views.dashboard,name='dashboard'),
    path('busdetails',views.busdetails,name='busdetails'),
    path('addbus',views.addbus,name='addbus'),
    path('cancelbus',views.cancelbus,name='cancelbus'),
    path('customerdetails',views.customerdetails,name='customerdetails'),
    path('logout',views.log_out,name='logout'),

]