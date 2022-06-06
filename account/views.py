from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                auth_login(request, user)
                return HttpResponse("Konto zalogowane")
            else:
                return HttpResponse("Konto nie istnieje")
    else:
        form = LoginForm()
        return render (request, 'registration/login.html', {'form': form})



@login_required
def dashboard(request):
    return render(request,"dashboard.html", {'section' : 'dashboard'})