from django.shortcuts import render, redirect
from django.contrib.auth import forms, login, authenticate, logout
from django.contrib.auth.models import User
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib import messages
from .forms import RegistrationForm


def index(request):
    print('index')
    context = {}
    # messages.add_message(request, messages.ERROR, 'index')
    return render(request, 'index.html', context)


class RegisterView(View):
    form = RegistrationForm

    def get(self, request):
        context = {
            'form': self.form(),
        }
        return render(request, 'dashboard/register.html', context)

    def post(self, request):
        print('RegisterView#post', request.POST)
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Registered.')
            return redirect('/dispatch')
        else:
            context = {
                'form': form
            }
            return render(request, 'dashboard/register.html', context)


class MainView(View):
    def get(self, request):
        print('MainView#get_redirect_url')
        pattern_name = '/dashboard'
        return redirect(pattern_name)


class LoginView(View):
    form = forms.AuthenticationForm

    def get(self, request):
        print('LoginView#get')
        context = {
            'form': self.form(),
        }
        return render(request, 'dashboard/login.html', context)

    def post(self, request):
        print('LoginView#POST', request.POST)
        form = self.form(None, request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            print('form validation ok')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            print('user', user)
            if user is not None:
                login(request, user)
                print('login ok')
                messages.add_message(request, messages.SUCCESS, 'Logged in')
                return redirect('/dispatch')
            else:
                messages.add_message(request, messages.WARNING, 'Failed log in')
                return render(request, 'dashboard/login.html', context)
        else:
            messages.add_message(request, messages.WARNING, 'Failed log in')
            return render(request, 'dashboard/login.html', context)


class Logout(View):
    def get(self, request):
        print('logout')
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'Logged out. Thank you for using.')
        return redirect('/')


class UserDashboardView(ListView):
    model = User
    template_name = 'dashboard/user_list.html'

    def get_context_data(self, **kwargs):
        context = super(UserDashboardView, self).get_context_data(**kwargs)
        print('context', context)
        return context


class UserCreateView(View):
    form = RegistrationForm

    def get(self, request):
        if not request.user.is_superuser:
            messages.add_message(request, messages.WARNING, 'not allowed')
            return redirect('/dashboard')
        context = {
            'form': self.form(),
        }
        return render(request, 'dashboard/create_user.html', context)

    def post(self, request):
        print('UserCreateView#post', request.POST)
        if not request.user.is_superuser:
            messages.add_message(request, messages.WARNING, 'not allowed')
            return redirect('/dashboard')
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'created.')
            return redirect('/dashboard')
        else:
            context = {
                'form': form
            }
            return render(request, 'dashboard/create_user.html', context)


class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name']


