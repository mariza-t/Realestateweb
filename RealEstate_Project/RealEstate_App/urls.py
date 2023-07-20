# from django.contrib import admin
from django.urls import include, path
from .import views
from  myadmin.views import AboutView,registerview,loginview

urlpatterns = [
   path('', views.home_view, name='index'),
   path('admin1/',AboutView.as_view(),name='admin1'),
   #path('admin1/chart/', chart_view.as_view(), name='chart'),
   path('about', views.about, name='about'),
   path('contact', views.contact, name='contact'),
   path('service_view/', views.service_view, name='service_view'),
   path('gallery_view/', views.gallery_view, name='gallery_view'),
   path('Property_detail_view/', views.Property_detail_view, name='Property_detail_view'),
   # path('login/', loginview.as_view(), name='login_urls'),
   # path('register/', registerview.as_view(), name='register_urls'),
 
] 

