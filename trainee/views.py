from django.shortcuts import render,redirect
from .models import*

trainees = []
def add_trainee(req):
    if req.method == 'POST':
        name = req.POST['name']
        email = req.POST['email']
        age = req.POST['age']
        Trainee.objects.create(name=name,email=email,age=age)
        return redirect('trainee_list')
    return render(req,'trainee/add_trainee.html')

def update_trainee(req, id):
    trainee = Trainee.objects.get(id=id)
    if not trainee:
        return redirect('trainee_list')
    
    if req.method == 'POST':
        trainee.name = req.POST['name']
        trainee.email = req.POST['email']
        trainee.age = req.POST['age']
        trainee.save()
        return redirect('trainee_list')
    
    return render(req, 'trainee/update_trainee.html', {'trainee': trainee})


def trainee_list(req):
    trainees=Trainee.objects.all()
    return render(req,'trainee/trainee_list.html',{'trainees':trainees})

def delete_trainee(req,id):
    Trainee.objects.get(id=id).delete()
    return redirect('trainee_list')

