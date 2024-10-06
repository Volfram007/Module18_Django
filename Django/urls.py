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
from task3.views import index3, shop3, cart3
from task4.views import index4, shop4, cart4
from task5.views import sign_up_by_html, sign_up_by_django

urlpatterns = [
    path('admin/', admin.site.urls),
    # task1
    path('', index, name='index'),
    # task2
    path('class-view/', ClassTemplate.as_view()),
    path('function-view/', func_template),
    # task3
    path('index3/', index3, name='index3'),
    path('shop3/', shop3, name='shop3'),
    path('cart3/', cart3, name='cart3'),
    # task4
    path('index4/', index4, name='index4'),
    path('shop4/', shop4, name='shop4'),
    path('cart4/', cart4, name='cart4'),
    # task5
    path('html_register', sign_up_by_html, name='sign_up_by_html'),
    path('django_register', sign_up_by_django, name='sign_up_by_django'),
]
