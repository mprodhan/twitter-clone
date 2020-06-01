from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from authentication.forms import LoginForm, SignUpForm

def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data["username"],
                password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage"))
                )
    form = LoginForm()
    return render(request, "loginpage.html", {"form": form})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse("loginpage"))

def signupview(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = TwitterUser.objects.create_user(
                username = data["username"],
                password = data["password"],
                display_name = data["display_name"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("loginpage"))
    form = SignUpForm()
    return render(request, "signuppage.html", {"form": form})
