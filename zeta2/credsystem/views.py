from django.shortcuts import render
from .forms import UserSignupForm

# Create your views here.


# signup view

def user_signup(request):
    if request.method=='POST':
        fm = UserSignupForm(request,request.POST)
        if fm.is_valid():
            fm.save()
            return render(request,'zeta2/signup.html',{'form':fm})
    else:
        fm = UserSignupForm()
    return render(request,'zeta2/signup.html',{'form':fm})