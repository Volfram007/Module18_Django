"""
URL configuration for Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from task2.views import index, ClassTemplate, func_template
from task3.views import index3, shop, cart

urlpatterns = [
    path('admin/', admin.site.urls),
    # task1
    path('', index),
    # task2
    path('class-view/', ClassTemplate.as_view()),
    path('function-view/', func_template),
    # task3
    path('index-shop/', index3, name='index'),
    path('shop/', shop, name='shop'),
    path('cart/', cart, name='cart'),
    # task4
]
