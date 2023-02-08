from django.urls import path
from .views import *

urlpatterns = [
    path('',homepage,name='home'),
    path('signup/',signuppage,name = 'signup'),
    path('login/',loginpage,name='login'),
    path('logout/',logoutpage,name='logout'),
    path('report/',reportpage,name='report'),
    path('createrecord/',createrecordpage,name='createrecord'),
]
