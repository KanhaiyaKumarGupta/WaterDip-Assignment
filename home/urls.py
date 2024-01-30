"""
URL configuration for home project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student.views.createtask import createTask
from student.views.getTasks import getAllTasks
from student.views.taskbyId import getTaskById
from student.views.deletetask import deleteTaskById
from student.views.updatetask import updateTask
from student.views.bulk_insert import bulk_insert_tasks

urlpatterns = [
    path("admin/", admin.site.urls),
    path("v1/tasks", createTask, name="createTask"),
    path("v1/tasks", getAllTasks, name="getAllTasks"),
    path("v1/tasks/<int:task_id>", getTaskById, name="getTaskById"),
    path("v1/tasks/<int:task_id>", deleteTaskById, name="deleteTaskById"),
    path("v1/tasks/<int:task_id>", updateTask, name="updateTask"),
    path("bulkinsert/tasks/", bulk_insert_tasks, name="bulk_insert_tasks"),
]
