from django.shortcuts import render

# Create your views here.
def admin_page(request):
    return render(request, 'admin_page.html')
def user_page(request):
    return render(request, 'user_page.html')
def index(request):
    return render(request, 'index.html')