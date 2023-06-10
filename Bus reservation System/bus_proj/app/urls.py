from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.loginpage, name="index"),
    path("accounts/login/", auth_views.LoginView.as_view()),
    path('sign_up',views.signin,name='sign_up'),
    path('home/',views.home,name='home'),
    #path('mybooking',views.mybookings,name='mybooking'),
    path('booking', views.bookingpage, name="login_details"),
    path('book',views.book,name='booking'),
    path('cancellation', views.cancellation, name="cancellation"),
    path('cancel',views.cancel,name='cancel'),
    path('logout',views.log_out,name="logout"),
    path('seat/', views.seat_selection, name='seat'),
    path('confirm/<str:id>', views.confirm, name='confirm'),
    path('seat/<int:id>/', views.seat_selection, name='seat_with_id'),
  

]
