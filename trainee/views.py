from django.shortcuts import render,redirect

trainees = []
def add_trainee(req):
    if req.method == 'POST':
        name = req.POST['name']
        email = req.POST['email']
        age = req.POST['age']
        id = len(trainees)+1
        trainees.append({'id':id,'name':name,'email':email,'age':age})
        return redirect('trainee_list')
    return render(req,'trainee/add_trainee.html')

def update_trainee(req, id):
    global trainees
    trainee = next((t for t in trainees if t['id'] == id), None)
    if not trainee:
        return redirect('trainee_list')
    
    if req.method == 'POST':
        trainee['name'] = req.POST['name']
        trainee['email'] = req.POST['email']
        trainee['age'] = req.POST['age']
        return redirect('trainee_list')
    
    return render(req, 'trainee/update_trainee.html', {'trainee': trainee})


def trainee_list(req):
    return render(req,'trainee/trainee_list.html',{'trainees':trainees})

def delete_trainee(req,id):
    global trainees 
    trainees = [t for t in trainees if t['id'] != id]
    return redirect('trainee_list')

