from django.shortcuts import render
from django.views import View

# Create your views here.
def admin_page(request):
    return render(request, 'admin_page.html')
def user_page(request):
    return render(request, 'user_page.html')

Aarr = ['Srinivas','Anjana','Ravi','Nagesh','Gayatri','Sobha Rani','Jyothi','PSrinivas','Pavan','Nagendra','Swarna']
Uarr =['Trisha','Shivani','Hemanth']

class index(View):
    def get(self, request):
        return render(request, 'index.html')
    def post(self, request):
        uname= request.POST.get("uname")
        upwd= request.POST.get("upwd")
        aname= request.POST.get("aname")
        apwd= request.POST.get("apwd")
        if (uname in Uarr and upwd == "webcap"):
            return render(request, 'User_sempage.html')
        elif (aname in Aarr and apwd == "webcap"):
            return render(request, 'Admin_sempage.html')
        return render(request, 'index.html')


# class index(View):
#     def get(self, request):
#         return render(request , 'index.html')
#     def post(self, request):
#         return render(request, 'admin_page.html')