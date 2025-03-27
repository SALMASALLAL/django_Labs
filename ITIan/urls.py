"""
URL configuration for ITIan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from .views import home, login, register
from rest_framework.routers import SimpleRouter
from course.views import CourseViewSet
from trainee.views import TraineeListAPI, AddTraineeAPI, UpdateTraineeAPI, DeleteTraineeAPI

router = SimpleRouter()
router.register('api/course', CourseViewSet, basename='course')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',home,name='home'),
    path('',register),
    path('trainee/',include('trainee.urls')),
    path('course/',include('course.urls')),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('api/trainee/', TraineeListAPI.as_view(), name='trainee_list_api'),
    path('api/trainee/add/', AddTraineeAPI.as_view(), name='add_trainee_api'),
    path('api/trainee/update/<int:pk>/', UpdateTraineeAPI.as_view(), name='update_trainee_api'),
    path('api/trainee/delete/<int:pk>/', DeleteTraineeAPI.as_view(), name='delete_trainee_api'),
] + router.urls
