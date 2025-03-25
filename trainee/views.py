from django.shortcuts import render,redirect
from .models import*
from course.models import Course
from .forms import TraineeForm
trainees = []
def add_trainee(req):
    context={
        'courses':Course.get_all_courses(),'form':TraineeForm()
    }
    if req.method == 'POST':
        name = req.POST['name']
        email = req.POST['email']
        age = req.POST['age']
        course=Course.get_course_by_id(req.POST['course'])
        Trainee.objects.create(name=name,email=email,age=age,course=course)
        return redirect('trainee_list')
    return render(req,'trainee/add_trainee.html',context)

def update_trainee(req, id):
    trainee = Trainee.objects.get(id=id)
    context={'courses':Course.get_all_courses(), 'trainee':trainee}
    if not trainee:
        return redirect('trainee_list')
    
    if req.method == 'POST':
        trainee.name = req.POST['name']
        trainee.email = req.POST['email']
        trainee.age = req.POST['age']
        trainee.course=Course.get_course_by_id(req.POST['course'])
        trainee.save()
        return redirect('trainee_list')
    
    return render(req, 'trainee/update_trainee.html',context=context)


def trainee_list(req):
    trainees=Trainee.objects.all()
    return render(req,'trainee/trainee_list.html',{'trainees':trainees})

def delete_trainee(req,id):
    Trainee.objects.get(id=id).delete()
    return redirect('trainee_list')

