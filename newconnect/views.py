from django.shortcuts import render,redirect
from django.http import HttpResponse as hr
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.contrib.auth.models import User
#def index(request):
    #return render(request,"index.html")
def Login(request):
    if request.user.is_authenticated: # to check if you are already logged in
        return redirect("UserProfile",request.user.username) #inside redirect u passes name of page where u have to go
    form = AddUserForm()
    error=False
    if request.method == "POST":
        data=request.POST
        un=data["un"]   # to access the data
        ps=data["ps"]
        usr=authenticate(username=un, password=ps)  #to check that datas that you have entered is there any user exist for that data
        if usr!=None:
            login(request,usr)  #to login with that username and pass
            return redirect("UserProfile",usr.username)
        error=True  # if you enters wrong username ans pass
    dict={"error":error,"form":form}

    return render(request,"login-register.html",dict)
def Register(request):
    if request.method == "POST":
        form = AddUserForm(request.POST, request.FILES) #call the form for files differently
        if form.is_valid(): #check if ur form is valid
            data = form.save(commit=False) #saving ecerything in data
            un = request.POST["un"]
            ps = request.POST["ps"]
            email = data.email
            usr = User.objects.create_user(un, email, ps)
            data.usr = usr
            data.save()
            return redirect("login")

        return hr("get Registered")

def Logout(request):
    logout(request)
    return redirect("login")
def UserProfile(request, Username): # redirect to page of logged nin user
    if not request.user.is_authenticated:
        return redirect("login")
    usr = User.objects.filter(username = Username) #to check whether your username exist with your entered data
    if not usr:
        loggen_in_username=request.user.username #to replace your entered wrong username with right username
        return redirect("UserProfile", loggen_in_username)
    print(usr)
    Usr = usr[0] #your usr will be list so u have to acces only 1st name from that
    print(Usr)
    User_Detail = UserDatas.objects.filter(usr = Usr)
    print(User_Detail)
    dict={
        "profile":User_Detail
    }
    print(dict)
    return render(request, "user_details.html", dict)
def Update_User_Details(request,Username):
    if not request.user.is_authenticated:
        return redirect("login")
    loggen_in_username = request.user.username
    if Username!=loggen_in_username:#to check the one who is logged in can only edit details
        return redirect("UserProfile", loggen_in_username)
    usr = User.objects.filter(username = Username)
    Usr = usr[0]
    User_Detail = UserDatas.objects.filter(usr=Usr)
    form=Edit_User_Details(request.POST or None, request.FILES or None,instance=User_Detail)
    if form.is_valid():
        form.save()
        return redirect("UserProfile", loggen_in_username)
    dict={
        "profile":User_Detail,"form":form
    }
    return redirect(request,"Update_User_Details.html",dict)



