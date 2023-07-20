# from django.contrib import admin
from django.urls import path
from .import views 
urlpatterns = [
   # path('admin1/', views.AboutView, name='home'),
   # path('tables',views.admintable,name="admintable"),
   # path('profile',views.adminprofile,name="adminprofile"),
   # path('admin1/chart/', views.chart_view, name='chart'),


   path('addservice/',views.service_form,name="service_urls"),
   path('delete/<str:pk>/',views.deleteservice, name="delete_url"),
   path('addimage/',views.gallery_form,name="gallery_urls"),
   path('addproperty/',views.property_form, name="property_urls"),
   path('addreadme/',views.readme_form, name="readme_urls"),
   path('addagents/',views.agent_form, name="agents_urls"),
   path('addcomments/',views.comment_form, name="comment_urls"),
   path('selledpro/',views.selled_form, name="selled_urls"),
   path('rentalpro/',views.rental_form, name="rental_urls"),
   path('appointment/',views.appointemnt_form, name="appointment_urls"),
   path('login/', views.loginview, name='login_urls'),
   path('register/', views.registerview, name='register_urls'),


] 
