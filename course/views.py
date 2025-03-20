from django.shortcuts import render,redirect

courses=[]
def add_course(req):
    if req.method=='POST':
        name = req.POST['name']
        description = req.POST['description']
        duration = req.POST['duration']
        id = len(courses)+1
        courses.append({'id':id,'name':name, 'description':description,'duration':duration})
        return redirect('course_list')
    return render(req,'course/add_course.html')

def update_course(req, id):
    global courses
    course = next((c for c in courses if c['id'] == id), None)
    if not course:
        return redirect('course_list')
    
    if req.method == 'POST':
        course['name'] = req.POST['name']
        course['description'] = req.POST['description']
        course['duration'] = req.POST['duration']
        return redirect('course_list')
    
    return render(req, 'course/update_course.html', {'course': course})

def course_list(req):
    return render(req,'course/course_list.html',{'courses':courses})

def delete_course(req,id):
    global courses
    courses=[c for c in courses if c['id'] != id]
    return redirect('course_list')