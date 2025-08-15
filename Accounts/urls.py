from django.urls import path
from .views import *


urlpatterns=[
     path("signUp/",signUp_view,name="signUp"),
     path("",login_view,name="login"),
     path("logout/",logout_view,name="logout"),
]