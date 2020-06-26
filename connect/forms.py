from django import forms
from .models import *
class AddUserForm(forms.ModelForm):
    class Meta:
        model = UserData
        exclude = ("usr", "dob", "location", "experience", "degree","profile_title","website","facebook","linkedin","twitter","instagram")
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
             "email":forms.EmailInput(attrs={"class":"form-control"}),
            "contact":forms.NumberInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
            "about":forms.Textarea(attrs={"class":"form-control", "rows":"5"})
        }
class Edit_User_Details(forms.ModelForm):
    class Meta:
        model = UserData
        exclude = ("usr",)
        widgets={
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "contact": forms.NumberInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "about": forms.Textarea(attrs={"class": "form-control", "rows": "5"}),
            "dob": forms.DateInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "experience": forms.TextInput(attrs={"class": "form-control"}),
            "degree": forms.TextInput(attrs={"class": "form-control"}),
            "profile_title":forms.TextInput(attrs={"class": "form-control"}),
            "website":forms.TextInput(attrs={"class": "form-control"}),
            "facebook":forms.URLInput(attrs={"class": "form-control"}),
            "twitter":forms.URLInput(attrs={"class": "form-control"}),
            "linkedin":forms.URLInput(attrs={"class": "form-control"}),
            "instagram":forms.URLInput(attrs={"class": "form-control"}),

        }

class StartCompany_Form(forms.ModelForm):
    class Meta:
        model = Company_Model
        exclude = ("usr",)
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control", }),
            "website":forms.TextInput(attrs={"class":"form-control", }),
            "address":forms.TextInput(attrs={"class":"form-control", }),
            "title":forms.TextInput(attrs={"class":"form-control", }),
            "map_embad":forms.Textarea(attrs={"class":"form-control", }),
            "map_url": forms.URLInput(attrs={"class": "form-control", }),
            "email":forms.EmailInput(attrs={"class":"form-control", }),
            "number":forms.NumberInput(attrs={"class":"form-control", }),
            "logo":forms.FileInput(attrs={"class":"form-control","onchange":"loadFile(event)" }),

        }

class UserBlog_Form(forms.ModelForm):
    class Meta:
        model = Blogs_Model
        exclude = ("usr",)
        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control", }),
            "youtube_video":forms.Textarea(attrs={"class":"form-control", }),
            "blog":forms.Textarea(attrs={"class":"form-control", })

        }