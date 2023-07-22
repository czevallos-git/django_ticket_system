from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm


def register_page(request):
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("tickets_page")
        else:
            messages.error(request, "An error occurred during registration")

    return render(request, "register.html", context={"form": form})


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        # Avoid individual error messages for usernames and passwords which might confirm the existence of the username.
        # A safer approach to prevent user enumeration is to return a generic error message when a login attemp fails.
        # Ensure all paths (login attempt failure or sucess) take the same time, so attackers are not alerted of the existence of the username.
        # Use time consuming hashing functions even if the username is wrong.
        # try:
        #     user = User.objects.get(username=username)
        # except Exception as e:
        #     pass

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("tickets_page")
        else:
            messages.error(request, "Username or password does not exist")

    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("home_page")
