from django.shortcuts import render


def index(request):
    print('index')
    context = {}
    return render(request, 'index.html', context)
