from django.shortcuts import render

#login view
def login_view(request):
    return render(request, 'login.html')
#home view
def home_view(request):
    return render(request, 'home.html')
