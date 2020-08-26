from django.shortcuts import render, HttpResponseRedirect, reverse
from homepage.models import CustomUser
from homepage.forms import SignUpForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from custom_users.settings import AUTH_USER_MODEL
# Create your views here.

def index(request):
    return render(request, 'index.html', {'auth_user_model': AUTH_USER_MODEL})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_custom_user = CustomUser.objects.create(username=data.get('username'), displayname=data.get('displayname'), password=data.get('password'))
            login(request, new_custom_user)
            return HttpResponseRedirect(reverse('homepage'))
    form = SignUpForm()
    return render(request, 'forms.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get('username'), password=data.get('password'))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
    form = LoginForm()
    return render(request, 'forms.html', {'form': form})
