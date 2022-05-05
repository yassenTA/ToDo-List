from pickle import NEXT_BUFFER
from unicodedata import name
from django import views
from django.urls import path
from .views import TaskDelete, TaskDetail, TaskList,TaskCreate,TaskUpdate,CustomLoginView,RegisterPage,TaskReorder
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',CustomLoginView.as_view(),name='login'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('task-create/',TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(),name='task-delete'),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('register/',RegisterPage.as_view(),name='register'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
]