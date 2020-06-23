from django import forms
from .models import *
class AddUserForm(forms.ModelForm):
    class Meta:
        model = UserDatas
        exclude = ("usr", "dob", "location", "experience", "degree")
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
             "email":forms.EmailInput(attrs={"class":"form-control"}),
            "contact":forms.NumberInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
            "about":forms.Textarea(attrs={"class":"form-control", "rows":"5"})
        }
class Edit_User_Details(forms.ModelForm):
    class meta:
        model=UserDatas
        exclude=("usr")
        widgets={
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "contact": forms.NumberInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "about": forms.Textarea(attrs={"class": "form-control", "rows": "5"}),
            "dob": forms.DateInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "experience": forms.TextInput(attrs={"class": "form-control"}),
            "degree": forms.TextInput(attrs={"class": "form-control"})
        }