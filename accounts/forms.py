from django import forms
from django.contrib.auth.models import User
from accounts.models import Contact

class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Enter Your Usernamae'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'*************'}))
    remember_me = forms.BooleanField(required=False)


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Enter Your First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Enter Your Last Name'}))
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Enter Your Username'}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'placeholder':'Enter a valid Email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'********************'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Repeat Your Password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
    
    def clean_password(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']

        if password != password2:
            raise forms.ValidationError('password does not match')
        return password2
    

      
    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username=data).exists():
            raise forms.ValidationError('Username already exists')
        return data
    
    def clean_email(self):
        data1 = self.cleaned_data['email']
        if User.objects.filter(email=data1).exists():
            raise forms.ValidationError('Email already exists')
        return data1
    

class ContactForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Enter Your Name'}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'placeholder':'Enter a Valid Email'}))
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message',]