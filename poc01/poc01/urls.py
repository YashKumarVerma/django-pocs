"""
URL configuration for poc01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from http.client import HTTPResponse
import sys
from django.urls import path
from django.http import HttpResponse

# 8 bit integers
large_data = list(range(40 * 1024 * 1024))

def raises_error(request):
    print("View that raises error")
    local_data = large_data
    raise ValueError

def does_not_raise_error(request):
    print("View that does not raise error")
    local_data = large_data    
    return HttpResponse("return this string")


urlpatterns = [
    path("raise_error/", raises_error),
    path("does_not_raise_error/", does_not_raise_error),
]
