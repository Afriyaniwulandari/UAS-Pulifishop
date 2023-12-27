from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('menu', views.menu, name='menu'),
    path('booking', views.booking, name='booking'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('contact', views.contact, name='contact'),
    
]