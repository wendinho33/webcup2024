from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from django.contrib import messages
from accounts.forms import LoginForm, RegisterForm, ContactForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'welcome' + ' ', request.user.username)
                return redirect('home')
            else:
                messages.warning(request, 'please try again!')
                return redirect('login')
        else:
            messages.error(request, 'please contact admin!!')
            return redirect('login')
    else:
        form = LoginForm()
        cx = {'form': form }
        template_name = 'accounts/login.html'
        return render(request, template_name, cx)

def user_logout(request):
    logout(request)
    return redirect('login')


def user_register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password2'])
            new_user.save()
            return redirect('login')
        else:
            return redirect('register')
    else:
        form = RegisterForm()
        cx = {'form': form}
        template_name = 'accounts/register.html'
        return render(request,template_name, cx)
    


def index_view(request):
    template_name = 'accounts/index.html'
    return render(request, template_name)


def whatsapp_login(request):
    waName = request.GET.get("waName")
    waNumber = request.GET.get("waNumber")
    # Split the string by space
    full_name = waName.split()
    if len(full_name) >= 2:
        # Extract the first and last words
        first_name = full_name[0]
        last_name = full_name[1]
    else:
        first_name = None
        last_name = None
    if User.objects.filter(username=waNumber).exists():
        w_user = User.objects.filter(username=waNumber).first()
        if w_user is not None:
            # If authentication is successful, log in the user
            login(request, w_user)
            return redirect("home")
    else:
        if first_name and last_name:
            w_user = User.objects.create_user(
                username=waNumber, first_name=first_name, last_name=last_name
            )
        else:
            w_user = User.objects.create_user(username=waNumber)
        if w_user is not None:
            # If authentication is successful, log in the user
            login(request, w_user)
            return redirect("home")
    return render(request, "accounts/register.html")



class Contact_Us(CreateView, SuccessMessageMixin):
    form_class = ContactForm
    template_name = 'accounts/contact.html'
    success_message = 'Your message has been sent successfully'
    success_url = reverse_lazy('home')


def about_us(request):
    return render(request, 'accounts/about.html')


def product(request):
    return render(request, 'accounts/products.html')