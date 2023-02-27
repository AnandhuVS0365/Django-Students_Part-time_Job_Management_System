from django.urls import path, include
from . import views
urlpatterns = [
   path('', views.index,name='home'),
   path('about/', views.about,name='about'),
   path('job/', views.job,name='job'),
   path('contact/', views.contact,name='contact'),
   path('department/', views.department,name='department'),
   path('login/', views.login,name='login'),
   path('application/', views.app),
   
   
   
   
   





]