from django import forms
from .models import *
class AddUserForm(forms.ModelForm):
    class Meta:
        model = UserData
        exclude = ("usr",)
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control",}),
             "email":forms.EmailInput(attrs={"class":"form-control",}),
            "contact":forms.NumberInput(attrs={"class":"form-control",}),
            "image":forms.FileInput(attrs={"class":"form-control",}),

            "about":forms.Textarea(attrs={"class":"form-control","rows":"5"})
        }
