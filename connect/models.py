from django.db import models
from django.contrib.auth.models import User
#we are crteating models to store oor data
class UserData(models.Model):
    usr=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True) #connecting User
    name=models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField(blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    about=models.TextField(max_length=150,blank=True,null=True)
    dob=models.DateField(null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    degree=models.CharField(max_length=100,null=True,blank=True)
    experience=models.CharField(max_length=100,null=True,blank=True)
    profile_title=models.CharField(max_length=200,null=True,blank=True)
    website=models.CharField(max_length=200,null=True,blank=True)
    facebook=models.URLField(null=True,blank=True)
    twitter=models.URLField(null=True,blank=True)
    linkedin=models.URLField(null=True,blank=True)
    instagram=models.URLField(null=True,blank=True)

    def __str__(self):
        return self.name

class Connections(models.Model):
    sender=models.ForeignKey(UserData,on_delete=models.CASCADE,related_name="sender",blank=True,null=True) #related name used because in one class u can use foriegn key for one object only to overcome these prblm use related name
    receiver=models.ForeignKey(UserData,on_delete=models.CASCADE,related_name="receiver",blank=True,null=True)
    status=models.CharField(max_length=30,null=True,blank=True,default="Sent")
    date=models.DateField(auto_now_add=True,null=True)


class Company_Model(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    number = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    map_url = models.URLField(null=True,blank=True)
    map_embad = models.TextField(null=True, blank=True)

class Blogs_Model(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    blog = models.TextField(null=True, blank=True)
    youtube_video = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)