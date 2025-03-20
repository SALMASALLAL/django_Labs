from django.urls import path
from .views import add_course,update_course,course_list,delete_course

urlpatterns = [
    path('add_course',add_course, name='add_course'),
    path('update_course/<int:id>',update_course,name='update_course'),
    path('course_list',course_list,name='course_list'),
    path('delete_course/<int:id>',delete_course,name='delete_course'),
    
]