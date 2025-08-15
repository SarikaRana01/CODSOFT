from .views import *
from django.urls import path


urlpatterns=[
    path("home/",home_view,name="home"),
    path("addTodo/",addTodo_view,name="add"),
    path("isCompleted/<int:id>/",isCompleted_view,name="isCompleted"),
    path("updateTodo/<int:id>/",updateTodo_view,name="update"),
    path("deleteTodo/<int:id>/",deleteTodo_view,name="delete"),
    path("priority/<str:priority>/",priority_view,name="priority"),
]