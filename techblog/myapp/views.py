from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import techblog
from .forms import techblogForm, loginForm


def blog(request):
    """Handles blog post creation and displaying all posts."""
    if request.method == 'POST':
        form = techblogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog post created successfully!")
            return redirect('myapp:main')
        else:
            messages.error(request, "Failed to create blog post. Please check your input.")
    else:
        form = techblogForm()

    posts = techblog.objects.all().order_by('-id')  
    return render(request, 'blog.html', {'form': form, 'posts': posts})


@login_required
def main(request):
    """Displays all blog posts in the main page."""
    data = techblog.objects.all()
    return render(request, 'main.html', {'data': data})


def post_detail(request, post_id):
    """Displays details of a single blog post."""
    post = get_object_or_404(techblog, id=post_id)  
    return render(request, 'post_detail.html', {'post': post})


def home(request):
    """Renders the home page."""
    return render(request, 'home.html')


def loginview(request):
    """Handles user login."""
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('myapp:main')
            else:
                messages.error(request, "Invalid username or password.")
                return redirect('myapp:login')  # Prevents rendering the form again with incorrect data.

    else:
        form = loginForm()

    return render(request, 'login.html', {'form': form})


def logoutview(request):
    """Handles user logout."""
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('myapp:login')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password

def createacc(request):
    """Handles user registration."""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')  # Get email from the form
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'createacc.html')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose another one.")
            return render(request, 'createacc.html')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered. Please use another email.")
            return render(request, 'createacc.html')

        # Create user with first_name, last_name, and email
        user = User.objects.create_user(
            username=username, 
            email=email,  # Add email
            password=password,  # No need to hash manually
            first_name=first_name, 
            last_name=last_name
        )

        messages.success(request, "Account created successfully! Please log in.")
        return redirect('myapp:login')

    return render(request, 'createacc.html')


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})



def update(request, id):
    """Handles updating an existing blog post."""
    obj = get_object_or_404(techblog, id=id)

    if request.method == 'POST':
        form = techblogForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog post updated successfully!")
            return redirect('myapp:main')
        else:
            messages.error(request, "Failed to update blog post.")

    else:
        form = techblogForm(instance=obj)

    return render(request, 'update.html', {'form': form})



def delete(request, id):
    """Handles deleting a blog post."""
    tech = get_object_or_404(techblog, id=id)
    tech.delete()
    messages.success(request, "Blog post deleted successfully!")
    return redirect('myapp:main')




def about(request):
    """Displays the about page."""
    context = {'year': datetime.now().year}
    return render(request, 'about.html', context)
