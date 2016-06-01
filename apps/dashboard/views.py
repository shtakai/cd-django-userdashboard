from django.shortcuts import render, redirect
from django.contrib.auth import forms
from django.views.generic import View
from django.views.generic.base import RedirectView


def index(request):
    print('index')
    context = {}
    return render(request, 'index.html', context)


class RegisterView(View):
    form = forms.UserCreationForm

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
            return redirect('/success')
        else:
            context = {
                'form': form
            }
            return render(request, 'dashboard/register.html', context)


class MainView(RedirectView):
    pattern_name = 'dashboard_main'

    def get_redirect_url(self, *args, **kwargs):
        print('MainView#get_redirect_url')
        return super(MainView, self).get_redirect_url(*args, **kwargs)
