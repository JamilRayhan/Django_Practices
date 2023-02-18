from django import forms
from django.core import validators


class user_form(forms.Form):
    user_email=forms.EmailField();
    user_Vmail=forms.EmailField();
    
    def clean(self):
        all_cleaned_data=super().clean()
        