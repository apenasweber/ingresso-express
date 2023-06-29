from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("dashboard")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def login(request):
    if request.method == "POST":
        # Process login form submission
        pass
    else:
        # Render login form
        pass
    return render(request, "login.html", {})


def password_reset(request):
    if request.method == "POST":
        # Process password reset form submission
        pass
    else:
        # Render password reset form
        pass
    return render(request, "password_reset.html", {})
