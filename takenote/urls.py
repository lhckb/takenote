"""takenote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', views.workInProgress),
    path('account/update', views.workInProgress),
    path('', views.index),
    path('login/', views.loginPage),
    path('login/submit/index', views.submitLoginIndex),
    path('login/submit/loginpage', views.submitLoginPage),
    path('logout', views.submitLogout),
    path('register/', views.register),
    path('register/submit/index', views.submitRegisterIndex),
    path('register/submit/registerpage', views.submitRegisterPage),
    path('notes/', views.notesPage),
    path('notes/add', views.addNote),
    path('notes/delete/<int:id>', views.deleteNote),
    path('notes/update/<int:id>/', views.updatePage),
    path('notes/update/<int:id>/submit', views.submitUpdate),
    path('notes/<int:id>/pin', views.pin)
]
