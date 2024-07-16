from django.urls import path, include
from .views import TaskDetailView,TaskListView



urlpatterns = [
    path('task/<int:pk>/',TaskDetailView.as_view(),name='task-detail'),
    path('tasks/',TaskListView.as_view(),name='tasks')
]
