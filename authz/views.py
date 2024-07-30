from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .forms import UserRegisterForm, UserLoginForm
from .serializers import UserSerializer


# Create your views here.

def main(request):
    user = request.user
    return render(request, 'home.html', {'user': user})


def LogoutUser(request):
    logout(request)
    return redirect(reverse('authz:main'))


class Register(View):
    def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('authz:main'))
        else:
            return render(request, 'register.html', {'form': form})


class Login(View):
    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('article:home'))
            else:
                return render(request, 'login.html', {'form': form})
        else:
            return render(request, 'login.html', {'form': form})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
