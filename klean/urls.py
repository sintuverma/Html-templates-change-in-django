"""klean URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from klean import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name="home"),
    path('about/', views.aboutPage, name="aboutus"),
    path('service/', views.servicePage, name="services"),
    path('project/', views.projectPage, name="project"),
    path('blog/', views.blogPage, name="blog"),
    path('blog-details/', views.blogDetails, name="blogDetails"),
    path('contactUs/', views.contactPage, name="contactUs"),
    path('saveFeedback/', views.saveForm, name="saveFeedback"),
]
