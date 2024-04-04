from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout


def register(request):
    # If the request method is POST, process the form data
    if request.method == "POST":
        # Create a form instance and populate it with data from the request
        form = UserCreationForm(request.POST)
        # Check if the form data is valid
        if form.is_valid():
            # Save the user to the database and log them in just afte registering   the user
            auth_login(request, form.save())
            # Redirect to the post listing page
            return redirect("posts:list")
            # form.save()
            #   return redirect("users:login")
    else:
        # If the request method is not POST, create a blank form
        form = UserCreationForm()

    # Render the registration form template with the form
    return render(request, "users/register.html", {"form": form})


def login(request):
    # If the request method is POST, process the form data
    if request.method == "POST":
        # Create a form instance and populate it with data from the request
        form = AuthenticationForm(data=request.POST)
        # Check if the form data is valid
        if form.is_valid():
            # Log the user in the form.get_user() method returns the authenticated user instance based on the credentials provided in the form. It doesn't fetch data from the database directly. Instead, it verifies the username and password provided in the form against the credentials stored in the authentication backend.
            auth_login(request, form.get_user())
            # Redirect to the next page if it exists
            next_page = request.POST.get("next")
            if next_page:
                return redirect(next_page)
            else:
                # If next_page is not specified, redirect to the default page
                return redirect("posts:list")
    else:
        # If the request method is not POST, create a blank form
        form = AuthenticationForm()

    # Render the login form template with the form
    return render(request, "users/login.html", {"form": form})


def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return redirect("users:login")
