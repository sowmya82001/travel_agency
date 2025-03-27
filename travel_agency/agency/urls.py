from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
    path('', views.tour_list, name='tour_list'),
    path('register/', views.customer_register, name='customer_register'),
    path('booking/<int:tour_id>/', views.make_booking, name='make_booking'),
]
