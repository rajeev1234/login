from django import forms
from .models import *



class Past_Work_form(forms.ModelForm):
    class Meta:
        model = Past_Work
        fields = ['Title','Company_Role','Image','Work_Status','From_Duration','Video','To_Duration']
