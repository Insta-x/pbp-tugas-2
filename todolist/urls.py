from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user
from todolist.views import create_task, add_task, finish_task, unfinish_task, delete_task, delete_task_ajax, show_task, get_task_json, amogus, test

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add/', add_task, name='add_task'),
    path('create-task/', create_task, name='create_task'),
    path('finish-task/<int:task_id>', finish_task, name='finish_task'),
    path('unfinish-task/<int:task_id>', unfinish_task, name='unfinish_task'),
    path('delete-task/<int:task_id>', delete_task, name='delete_task'),
    path('delete/<int:task_id>', delete_task_ajax, name='delete_task_ajax'),
    path('show-task/<int:task_id>', show_task, name='show_task'),
    path('json/', get_task_json, name='get_task_json'),
    path('amogus/', amogus, name='amogus'),
    path('test/<str:message>', test, name='test'),
]