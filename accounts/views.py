from django.shortcuts import render,redirect
from django.contrib.auth import login,logout 
from .forms import RegisterForm,CostomUserChangeForm 
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def register(request):
     if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
           user=form.save(commit=False)
           user.is_staff=True
           user=form.save()
           login(request,user)
           return redirect('checkout')
     else:
        form=RegisterForm()
     return render(request,'accounts/register.html',{'form':form})

    

def login_view(request):
    if request.method=='POST':
        form=CostomUserChangeForm(request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('checkout')
    else:
        form=CostomUserChangeForm()
    return render(request,'accounts/login.html',{'form':form})


def logout_view(request):
    logout(request)
    return redirect('index')
