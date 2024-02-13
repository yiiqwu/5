from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.
def info(request):
    return render(request, 'info.html')

def articles_detail(request):
    return render(request, 'articles_detail.html')

def registration(request):
    return render(request, 'registration.html')
def index(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
