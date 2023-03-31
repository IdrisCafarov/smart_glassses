
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
# from PIL import Image
# from user.models import *

# get custom user
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
        'placeholder':'your@example.com'
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

    # adress=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={
    #     'type':'text',
    #     'class':'form-control',
    #     'id':'adress',
    #     'placeholder':'Enter your Adress'

    #     }
    # ))

    # adress_2=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={
    #     'type':'text',
    #     'class':'form-control',
    #     'id':'adress2',
    #     'placeholder':'Enter your Adress'

    #     }
    # ))

    # country=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={
    #     'type':'password',
    #     'class':'form-control',
    #     'placeholder':'Enter your Password'
    #     }
    # ))

    # city=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={
    #     'type':'password',
    #     'class':'form-control',
    #     'placeholder':'Enter your Password'
    #     }
    # ))



    class Meta:
        model = MyUser
        fields = ('first_name','last_name','email')




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""
