"""
URL configuration for grocery_mart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from webapp import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.main),
    path('main',views.main),
    path('home', views.home),
    path('features', views.features),
    path('products', views.products),
    path('categories', views.categories),
    path('reviews', views.reviews),
    path('blogs', views.blogs),
    path('signup', views.signup),
    path('login', views.login),
    path('display',views.display)
]
