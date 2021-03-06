"""nhsee_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from nhsee.views import project_views, judge_views, student_views, judgeassignment_views
from nhsee import viewin

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'projects/',project_views.projectslisting),
    path(r'judges/',judge_views.judgeslisting),
    path(r'students/',student_views.studentlisting),
    path(r'assignment/',judgeassignment_views.judge_listing_assignment),
    path(r'home/',viewin.home),
    path(r'',viewin.home),
  #  path(r'api/assign/',views.assignjudge)
]
