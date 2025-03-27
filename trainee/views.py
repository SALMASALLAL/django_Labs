from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse_lazy
from .models import*
from course.models import Course
from .forms import TraineeForm
from django.views import View
from django.views.generic import ListView 
from django.views.generic.edit import DeleteView


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

# def add_trainee(req):
#     context={
#         'courses':Course.get_all_courses(),'form':TraineeForm()
#     }
#     if req.method == 'POST':
#         name = req.POST['name']
#         email = req.POST['email']
#         age = req.POST['age']
#         course=Course.get_course_by_id(req.POST['course'])
#         Trainee.objects.create(name=name,email=email,age=age,course=course)
#         return redirect('trainee_list')
#     return render(req,'trainee/add_trainee.html',context)

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

# def update_trainee(req, id):
#     trainee = Trainee.objects.get(id=id)
#     context={'courses':Course.get_all_courses(), 'trainee':trainee}
#     if not trainee:
#         return redirect('trainee_list')
    
#     if req.method == 'POST':
#         trainee.name = req.POST['name']
#         trainee.email = req.POST['email']
#         trainee.age = req.POST['age']
#         trainee.course=Course.get_course_by_id(req.POST['course'])
#         trainee.save()
#         return redirect('trainee_list')
    
#     return render(req, 'trainee/update_trainee.html',context=context)

class TraineeList(ListView):
    model=Trainee
    template_name='trainee/trainee_list.html'
    context_object_name='trainees'
    
# def trainee_list(req):
#     trainees=Trainee.objects.all()
#     return render(req,'trainee/trainee_list.html',{'trainees':trainees})

class DeleteTrainee(DeleteView):
    model = Trainee
    success_url = reverse_lazy('trainee_list')
    
# def delete_trainee(req,id):
#     Trainee.objects.get(id=id).delete()
#     return redirect('trainee_list')

