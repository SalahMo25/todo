from django.urls import path
from . import views
urlpatterns = [
    path('todo', views.todo , name='todo'  ),
    path('delete/<int:id>', views.remove , name='delete'  ),
]