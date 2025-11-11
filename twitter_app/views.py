from django.shortcuts import render

#login view
def login_view(request):
    return render(request, 'login.html')
#home view
def home_view(request):
    
    return render(request, 'home.html')
def signup_view(request):
    return render(request, 'signup.html')