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
    def __str__(self):
        return self.name

