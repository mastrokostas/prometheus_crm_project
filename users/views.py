from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def login_user(request):
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session.set_expiry(43200) #12 hours
            username = request.user.username.capitalize()
            messages.success(request, "You have been Logged in. Welcome, " + username+"!")
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
        else:
            messages.success(request, "There was an error logging in, please try again...")
            return redirect('login')
    else:
        return render(request, 'users/login.html')


@login_required(login_url= 'login')
def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('login')