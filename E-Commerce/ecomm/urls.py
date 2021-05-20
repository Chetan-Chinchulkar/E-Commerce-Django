from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='ecomm-home'),
    path('about/', views.about,name='ecomm-about'),
    path('order-success/',views.order,name='order-success'),
    
]