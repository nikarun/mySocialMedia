from django.shortcuts import render,redirect
from django.http import HttpResponse as hr
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.db.models import Q
from datetime import date
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
    dict={"error":error,
          "form":form}

    return render(request,"login-register.html",dict)
def Register(request):
    form=AddUserForm()
    if request.method == "POST":
        form = AddUserForm(request.POST, request.FILES) #call the form for files differently
        if form.is_valid(): #check if ur form is valid
            print(form)
            data = form.save(commit=False) #saving ecerything in data
            un = request.POST["un"]
            ps = request.POST["ps"]
            email = data.email
            usr = User.objects.create_user(un, email, ps)
            data.usr = usr
            data.save()
            return redirect("login")
    dict={"form":form}
    return render(request,"login-register.html",dict)





def Logout(request):
    logout(request)
    return redirect("login")
def UserProfile(request, Username): # redirect to page of logged nin user
    if not request.user.is_authenticated:
        return redirect("login")
    user = User.objects.filter(username = Username) #to check whether your username exist with your entered data
    if not user:
        loggen_in_username=request.user.username #to replace your entered wrong username with right username
        return redirect("UserProfile", loggen_in_username)
    connection=None
    if request.user.username != Username:
        user1=User.objects.get(username = Username)
        user2 = User.objects.get(username=request.user.username)
        UserData1=UserData.objects.get(usr=user1)
        UserData2 = UserData.objects.get(usr=user2)
        connection=Connections.objects.filter(Q(sender=UserData1,receiver=UserData2) | Q(sender=UserData2,receiver=UserData1))
        print(connection)
        print("you are not logged in User")
        if connection:
            connection=connection[0]
    Usr = user[0] #your usr will be list so u have to acces only 1st name from that

    User_data = UserData.objects.get(usr = Usr)

    dict={"profile":User_data,"connection":connection}

    return render(request, "user_details.html", dict)
def Update_User_Details(request,Username):
    if not request.user.is_authenticated:
        return redirect("login")
    loggen_in_username = request.user.username
    if Username != loggen_in_username:#to check the one who is logged in can only edit details
        return redirect("UserProfile", loggen_in_username)
    usr = User.objects.filter(username = Username)
    Usr = usr[0]
    User_Detail = UserData.objects.get(usr=Usr)
    form = Edit_User_Details(request.POST or None, request.FILES or None, instance=User_Detail)


    if form.is_valid():
        form.save()
        return redirect("UserProfile", loggen_in_username)
    dict={
        "profile":User_Detail,"form":form
    }
    return render(request,"Update_User_Details.html",dict)


def All_Profession(request,what):
    if not request.user.is_authenticated:
        return redirect("login")
    logged_in_user=User.objects.get(username=request.user.username)
    me=UserData.objects.get(usr=logged_in_user)

    data=""
    if what == "all":
        data = UserData.objects.all()
    if what == "Request":
        connection = Connections.objects.filter(receiver=me, status="Sent")
        User_Data = []
        for c in connection:
            ud = UserData.objects.get(id=c.sender.id)
            User_Data.append(ud)
        data = User_Data

    if what == "Sent":
        connection = Connections.objects.filter(sender=me,status="Sent")
        User_Data = []
        for c in connection:
            ud = UserData.objects.get(id=c.receiver.id)
            User_Data.append(ud)
        data = User_Data
    if what == "Friends":
        connection = Connections.objects.filter(Q(sender=me,status="friend") | Q(receiver=me,status="friend")).order_by("-date")
        Data = []
        for c in connection:
            User_Data = UserData.objects.get(id=c.sender.id)
            if User_Data.id != me.id:
                Data.append(User_Data)

            User_Data = UserData.objects.get(id=c.receiver.id)
            if User_Data.id != me.id:
                Data.append(User_Data)
            data = Data

    all_users=UserData.objects.all()
    dict={"allusers":data,"what":what}
    return render(request,"professionals.html",dict)

def Manage_Your_Connections(request,action,u_id):
    if not request.user.is_authenticated:
        return redirect("login")
    if action == "Send_Request":
        senderUser=User.objects.get(username=request.user.username)
        sender=UserData.objects.get(usr=senderUser)
        receiver=UserData.objects.get(id=u_id)
        Connections.objects.create(sender = sender, receiver = receiver)
        return redirect("UserProfile",receiver.usr.username)
    if action == "Accept_Request" or action == "Reject_Request":
        ReceiverUser = User.objects.get(username=request.user.username)
        receiver = UserData.objects.get(usr=ReceiverUser)
        sender = UserData.objects.get(id=u_id)
        connection = Connections.objects.filter(sender=sender, receiver=receiver)
        if connection:
            for c in connection:
                if action == "Accept_Request":
                    c.status = "friend"
                    c.save()
                if action == "Reject_Request":
                    c.status = "rejected"
                    c.save()

        return redirect("professionals", "all")

    return hr("you want"+str(action)+"for user"+str(u_id))