"""Selfproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from connect.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Login,name="login"),
    path('in/<str:Username>/',UserProfile,name="UserProfile"),
    path('in/Edit/<str:Username>/',Update_User_Details,name="UpdateUserDetails"),
    path('register/',Register,name="register"),
    path('Logout/',Logout,name="logout"),
    path('professionals/<str:what>/',All_Profession,name="professionals"),
    path('connections/<str:action>/<int:u_id>/',Manage_Your_Connections,name="connections"),
    path('professionals_html/<str:what>/',All_Professional_Html,name="allprofessionals_html"),
    path('addcompany/',Add_Company,name="addcompany"),
    path('Your_companydetails/',CompanyDetails,name="companydetails"),
    path('PostNewBlog/',NewPost,name="post")

    #path('index/',index,name="index")
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
