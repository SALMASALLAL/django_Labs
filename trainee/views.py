from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse_lazy
from .models import*
from course.models import Course
from .forms import TraineeForm
from django.views import View
from django.views.generic import ListView 
from django.views.generic.edit import DeleteView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import UpdateAPIView, DestroyAPIView
from .serializers import TraineeSerializer

class AddTrainee(View):
    def get(self,req):
        form=TraineeForm()
        context={'form':form}
        return render(req,'trainee/add_trainee.html',context)
    
    def post(self,req):
        form=TraineeForm(req.POST)
        if form.is_valid():
            Trainee.objects.create(name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                age=form.cleaned_data['age'],
                course=Course.get_course_by_id(form.cleaned_data['course']))
            return redirect('trainee_list')
        context={'form':form}
        return render(req,'trainee/add_trainee.html',context)
        
    
    
trainees = []

class UpdateTrainee(View):
    def get(self,req,id):
        context={'courses':Course.get_all_courses(), 'trainee':get_object_or_404(Trainee,id=id)}
        print(context['trainee'])
        return render(req, 'trainee/update_trainee.html',context)
    
    def post(self,req,id):
        trainee = get_object_or_404(Trainee,id=id)
        trainee.name = req.POST['name']
        trainee.email = req.POST['email']
        trainee.age = req.POST['age']
        trainee.course=Course.get_course_by_id(req.POST['course'])
        trainee.save()
        return redirect('trainee_list')

class TraineeList(ListView):
    model=Trainee
    template_name='trainee/trainee_list.html'
    context_object_name='trainees'
    
class DeleteTrainee(DeleteView):
    model = Trainee
    success_url = reverse_lazy('trainee_list')

class TraineeListAPI(APIView):
    def get(self, request):
        trainees = Trainee.objects.all()
        serializer = TraineeSerializer(trainees, many=True)
        return Response(serializer.data)

class AddTraineeAPI(APIView):
    def post(self, request):
        serializer = TraineeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateTraineeAPI(UpdateAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer

class DeleteTraineeAPI(DestroyAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer

