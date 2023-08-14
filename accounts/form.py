from django import forms
from django.contrib.auth.models import User

from .models import Profail,Comment
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
class RegistrationForms(forms.ModelForm):
    password=forms.CharField(label="parol",widget=forms.PasswordInput)
    password2=forms.CharField(label="parol takrorlang",widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','email']
        
        
    def clean_password2(self):
        data=self.cleaned_data
        if data['password']!=data['password2']:
            raise forms.ValidationError('parolingiz mos emas')
        return data['password2']


class ProfilEditForm(forms.ModelForm):
    class Meta:
        model=Profail
        fields=['photo']
        
        
class UserEditForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','email']
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['body']