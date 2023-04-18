from django.shortcuts import render
from django.views import View
import re
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        # Check which form was submitted
        if 'user' in request.POST:
            # First login form was submitted
            uname = request.POST.get('uname')
            upwd = request.POST.get('upwd')

            # Define regular expression patterns for username and password
            username_pattern = r'^[1-9][0-9]33[5 1][a A]12[0-9 a-z A-Z][0-9]$'
            password_pattern = r'^webcap$'

            # Validate username and password using regular expressions
            if not re.match(username_pattern, uname):
                return HttpResponse('Invalid username')
            elif not re.match(password_pattern, upwd):
                return HttpResponse('Invalid password')
            else:
                # Username and password are valid, do something here
                return user_sempage(request)
        elif 'admin' in request.POST:
            # Second login form was submitted
            aname = request.POST.get('aname')
            apwd = request.POST.get('apwd')

            # Define regular expression patterns for username and password
            adminname_pattern = r'^[1-9][0-9]331A12[0-9][0-9]$'
            apassword_pattern = r'^admin$'

            # Validate username and password using regular expressions
            if not re.match(adminname_pattern, aname):
                return HttpResponse('Invalid admin')
            elif not re.match(apassword_pattern, apwd):
                return HttpResponse('Invalid password')
            else:
                # Username and password are valid, do something here
                return admin_sempage(request)
    else:
        return render(request, 'index.html')


# Create your views here.
def admin_page(request):
    return render(request, 'admin_page.html')
def user_page(request):
    return render(request, 'user_page.html')

# user sempage 
def user_sempage(request):
    return render(request, 'User_sempage.html')
def admin_sempage(request):
    return render(request, 'Admin_sempage.html')
# sem 1
def Sem1_adminpage(request):
    return render(request, 'Sem1_adminpage.html')
def Sem1_userpage(request):
    return render(request, 'Sem1_userpage.html')
# sem 2
def Sem2_adminpage(request):
    return render(request, 'Sem2_adminpage.html')
def Sem2_userpage(request):
    return render(request, 'Sem2_userpage.html')
# sem 3
def Sem3_adminpage(request):
    return render(request, 'Sem3_adminpage.html')
def Sem3_userpage(request):
    return render(request, 'Sem3_userpage.html')
# sem 4
def Sem4_adminpage(request):
    return render(request, 'Sem4_adminpage.html')
def Sem4_userpage(request):
    return render(request, 'Sem4_userpage.html')
# sem 5
def Sem5_adminpage(request):
    return render(request, 'Sem5_adminpage.html')
def Sem5_userpage(request):
    return render(request, 'Sem5_userpage.html')
# sem 6
def Sem6_adminpage(request):
    return render(request, 'Sem6_adminpage.html')
def Sem6_userpage(request):
    return render(request, 'Sem6_userpage.html')
# sem 7
def Sem7_adminpage(request):
    return render(request, 'Sem7_adminpage.html')
def Sem7_userpage(request):
    return render(request, 'Sem7_userpage.html')


# class index(View):
#     def get(self, request):
#         return render(request , 'index.html')
#     def post(self, request):
#         return render(request, 'admin_page.html')

