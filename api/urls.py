from django.urls import path

from api import views

urlpatterns = [
    path('todos/', views.TodoListCreate.as_view()),
    path('todos/<int:pk>', views.TodoReviewUpdateDestroy.as_view())
]
