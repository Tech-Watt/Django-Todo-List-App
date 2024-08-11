from django.urls import path 
from . import views
urlpatterns = [
path('',views.homepage,name='homepage'),
path('create_todo/',views.create_todo,name='create_todo'),
path('view_todo/',views.view_todo,name='view_todo'),
path('edit_todo/<int:todo_id>',views.edit_todo,name='edit_todo'),
]