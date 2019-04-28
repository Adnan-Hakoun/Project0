from django.shortcuts import render , redirect
from .forms import Sign_in , Sign_up
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User



# def get_users(request):
#     users=User.objects.all()
#     return render(request,'users.html',{'users':users})

def user_profile(request,*args,**kwargs):
    if not request.user.is_authenticated:
        return redirect('/sign_in/') #we used not just to shorten the code nut we can use the if normally and put all the logic inside the if
    if request.GET:
        pass
    return render(request,'profile.html')

def sign_up(request):
    if request.POST:
        form=Sign_up(request.POST)
        if form.is_valid():
            user=User.objects.create(username=request.POST['username'])
            user.set_password(request.POST['password'])
            user.save()
            login(request,user)
            return redirect('/products/')
    empty_form=Sign_up()
    return render(request,'sign_up.html',{'empty_form':empty_form})


def sign_in(request):
    if request.user.is_authenticated:
        return redirect ('/products/')

    if request.POST:
        form=Sign_in(request.POST)
        theuser=authenticate(request,username=request.POST['username'],
                             password=request.POST['password'])
        if theuser:
            login(request,theuser)
            return redirect('/products/')
        else:
            return redirect('/users/sign_in/')

    empty_form=Sign_up()
    return render(request,'sign_in.html',{'empty_form':empty_form})



def sign_out(request):
    if request.user:
        logout(request)
        return redirect('/users/sign_in/')
