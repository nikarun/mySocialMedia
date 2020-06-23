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

