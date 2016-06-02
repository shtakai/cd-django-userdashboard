"""userdashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^$', views.index, name='dashboard_index'),
    url(r'^signup$', views.LoginView.as_view(), name='dashboard_signin'),
    url(r'^register$', views.RegisterView.as_view(), name='dashboard_register'),
    url(r'^dispatch$', views.MainView.as_view()),
    url(r'^main$', login_required(views.index, login_url='/signup'), name='dashboard_main'),
    url(r'^logout$', login_required(views.Logout.as_view(), login_url='/signup'), name='logout'),
    url(r'^dashboard$', login_required(views.UserDashboardView.as_view(), login_url='/signup'), name='dashboard_user'),
    url(r'^user/new', login_required(views.UserCreateView.as_view(), login_url='/signup'), name='dashboard_create_user'),
]
