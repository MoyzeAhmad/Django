from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    # Your view code here
    return render(request, 'polls/index.html')
def register(request):
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('polls:index')
  else:
    form = RegisterForm()
  return render(request, 'polls/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('polls:index')
    else:
        form = LoginForm()
    return render(request, 'polls/login.html', {'form': form})

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('polls:index')

