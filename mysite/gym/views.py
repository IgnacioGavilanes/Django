from django.shortcuts import render
from gym.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from gym.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home (request):
    return render(request, "index.html")

def about (request):
    return render(request, "about.html")

def contact (request):
    return render(request, "contact.html")

def user_login (request):
    if not request.user.is_anonymous:
        return HttpResponseRedirect('/private')
    elif request.method == 'POST':
        form = AuthenticationForm (request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            access = authenticate(username=username, password=password)
            if access is not None:
                if access.is_active:
                    login(request, access)
                    return HttpResponseRedirect('/private')
            else:
                return render(request, "failed_login.html")
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {'form': form})

@login_required(login_url= "/login")
def private (request):
    username = request.user
    return render(request, 'private.html', {'username': username})

def exit(request):
    if not request.user.is_anonymous:
        logout(request)
        return HttpResponseRedirect('/login')

def profile (request):
    return render(request, "profile.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Email"
            content = form.cleaned_data['message'] + '\n'
            content += "Communicate to: " + form.cleaned_data['email']
            email = EmailMessage(subject, content, to=["nachogavilanes30@gmail.com"])
            try:
                email.send()
                return render(request, 'sent_email.html')
            except:
                return render(request, 'failed_email.html')
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})

def new_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        try:
            form.save()
            return render(request, "user_created.html")
        except:
            return render(request, "user_creation_failed.html")
    else:
        form = UserCreationForm()
        return render(request, "new_user.html", {'form': form})

def search(request):
    if 'input' in request.GET and request.GET ['input']:
        query = request.GET['input']
        trainers = Trainer.objects.filter(firstName__contains=query)
        return render(request, 'results.html', {'trainers':trainers})
    else: 
        return render(request, 'results.html')

def error_404 (request, exception):
    return render(request, '404.html', {})

def error_500 (request):
    return render(request, '500.html', {})