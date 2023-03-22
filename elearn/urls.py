"""elearn URL Configuration

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
from ebook.views import *
from ebook import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , index.as_view(), name="index1"),
    path('admin_page/' , views.admin_page, name="index2"),
    path('user/' , views.user_page, name="index3"),
    path('Sem-1_userpage/' , views.admin_page, name="index4"),
    path('Sem-1_adminpage/' , views.user_page, name="index5"),
    path('Sem-2_userpage/' , views.admin_page, name="index6"),
    path('Sem-2_adminpage/' , views.user_page, name="index7"),
    path('Sem-3_userpage/' , views.admin_page, name="index8"),
    path('Sem-3_adminpage/' , views.user_page, name="index9"),
    path('Sem-4_userpage/' , views.admin_page, name="index10"),
    path('Sem-4_adminpage/' , views.user_page, name="index11"),
]
