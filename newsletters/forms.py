from django import forms
from .models import news



class newsform(forms.ModelForm):
    name =forms.CharField(max_length=100)
    email= forms.EmailField()


    class Meta:
        model = news
        fields = ["email","name" ]

