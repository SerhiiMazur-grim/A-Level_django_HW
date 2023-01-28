"""
Task application urls Configurstion

"""

from django.urls import path
from task.views import tast_list_view, task_detail_view


urlpatterns = [
    path('', tast_list_view, name='task_list'),
    path('<int:id>/', task_detail_view, name='task_detail'),
]


