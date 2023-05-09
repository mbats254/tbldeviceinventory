from django.urls import path

from . import views

urlpatterns = [
    path("", views.ApiOverview, name="api_overview"),
    path("user/", views.userApiOverview, name="user_api_overview"),
    path("admin/create/task", views.createTask, name="createTask"),
    path("admin/assign/task", views.assignTask, name="assignTask"),
    path("admin/all/tasks", views.allTasks, name="allTasks"),
    path("user/all/my/tasks", views.allMyTasks, name="allMyTasks"),
    path("user/single/task/<str:uniqid>", views.singleTask, name="singleTask"),

]