from django.shortcuts import render , redirect

def home(req):
    return render(req,'home.html')

def login(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        if username == 'salma' and password == '123':  
            return redirect('home')
        else:
            return render(req, 'login.html', {'error': 'Invalid credentials'})
    return render(req,'login.html')

def register(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        confirm_password = req.POST.get('confirm_password')
        if password != confirm_password:
            return render(req, 'register.html', {'error': 'Passwords do not match'})
        else:
            return redirect('login')

    return render(req, 'register.html')
