from django.urls import path
from .views import AddTrainee,UpdateTrainee,TraineeList,DeleteTrainee
urlpatterns = [
    path('add_trainee',AddTrainee.as_view(),name='add_trainee'),
    path('update_trainee/<int:id>',UpdateTrainee.as_view(),name='update_trainee'),
    path('trainee_list',TraineeList.as_view(),name='trainee_list'),
    path('delete_trainee/<int:pk>',DeleteTrainee.as_view(),name='delete_trainee'),
]

