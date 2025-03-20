from django.urls import path
from .views import add_trainee,trainee_list,update_trainee,delete_trainee
urlpatterns = [
    path('add_trainee',add_trainee,name='add_trainee'),
    path('update_trainee/<int:id>',update_trainee,name='update_trainee'),
    path('trainee_list',trainee_list,name='trainee_list'),
    path('delete_trainee/<int:id>',delete_trainee,name='delete_trainee'),
]
