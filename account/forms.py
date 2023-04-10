
from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from account.models import *

User = get_user_model()




class LoginForm(forms.Form):
    email= forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={
        'type':'email',
        'class':'form-control',
        'placeholder':'Enter your Email'
        }
    ))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={
        'type':'password',
        'class':'form-control',
        'placeholder':'Enter your Password'
        }
    ))

    def clean(self):
        email=self.cleaned_data.get('email')
        password=self.cleaned_data.get('password')
        if email and password:
            user=authenticate(email=email,password=password)
            if not user:
                raise forms.ValidationError('Email or Password is incorrect')




        return super(LoginForm, self).clean()



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""



class UpdateForm(forms.ModelForm):
    email= forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={
        'type':'email',
        'class':'form-control',
        'id':'email',
        'placeholder':'your@example.com',
        'readonly':True
        }
    ))

    phone= forms.CharField(max_length=100,widget=forms.NumberInput(attrs={
        'type':'text',
        'class':'form-control',
        'id':'email',
        'placeholder':'+9941111111',
        'readonly':True
        }
    ))

    adress= forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'type':'text',
        'class':'form-control',
        'id':'email',
        'placeholder':'City Street',
        }
    ))


    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'type':'email',
        'class':'form-control',
        'id':'firstName',
        'placeholder':'Enter your First Name'

        }
    ))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'type':'email',
        'class':'form-control',
        'id':'lastName',
        'placeholder':'Enter your Last Name'
        }
    ))

    image=forms.FileField(widget=forms.FileInput(attrs={
        'type':'file',
        'class':'form-file-input form-control',
        }
    ))


    class Meta:
        model = MyUser
        fields = ('first_name','last_name','email','image','phone','adress')




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""



class UserDiseaseForm(forms.ModelForm):

    description= forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'rows':'4',
        'id':'comment'
        }
    ))

    def __init__(self, *args,user, **kwargs):
        super(UserDiseaseForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""

        existing_user_diseases = UserDisease.objects.filter(user=user)
        existing_disease_ids = [user_disease.disease.id for user_disease in existing_user_diseases]
        available_diseases = Disease.objects.exclude(id__in=existing_disease_ids)
        self.fields['disease'].queryset = Disease.objects.exclude(id__in=existing_disease_ids)


    class Meta:
        model = UserDisease
        fields = ['disease', 'description']