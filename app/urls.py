from django.urls import path
from  .views import *
urlpatterns = [
   path('',register_user),
   path('Login/',user_login),
   path('logout/', user_logout, name='logout'),
]
