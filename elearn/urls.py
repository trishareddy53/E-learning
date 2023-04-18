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
    path('' , index, name="index1"),
    path('admin_page/' , views.admin_page, name="index2"),
    path('user/' , views.user_page, name="index3"),
    path('userSempage/', views.user_sempage, name='usersem'),
    path('adminSempage/', views.admin_sempage, name='adminsem'),
    path('Sem1_userpage/' , views.Sem1_userpage, name="index4"),
    path('Sem1_adminpage/' , views.Sem1_adminpage, name="index5"),
    path('Sem2_userpage/' , views.Sem2_userpage, name="index6"),
    path('Sem2_adminpage/' , views.Sem2_adminpage, name="index7"),
    path('Sem3_userpage/' , views.Sem3_userpage, name="index8"),
    path('Sem3_adminpage/' , views.Sem3_adminpage, name="index9"),
    path('Sem4_userpage/' , views.Sem4_userpage, name="index10"),
    path('Sem4_adminpage/' , views.Sem4_adminpage, name="index11"),
    path('Sem5_userpage/' , views.Sem5_userpage, name="index12"),
    path('Sem5_adminpage/' , views.Sem5_adminpage, name="index13"),
    path('Sem6_userpage/' , views.Sem6_userpage, name="index14"),
    path('Sem6_adminpage/' , views.Sem6_adminpage, name="index15"),
    path('Sem7_userpage/' , views.Sem7_userpage, name="index16"),
    path('Sem7_adminpage/' , views.Sem7_adminpage, name="index17"),
]
