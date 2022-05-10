from django.shortcuts import render, redirect
from .forms import DummyForm, CreateUser, LogUser, BlogForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Blog


# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    return render(request, 'home.html', context)


def contact(request):
    fm = DummyForm()
    context = {"form": fm}
    return render(request, 'contact.html', context)


def about(request):
    return render(request, 'about.html')


def signup(request):
    if request.method == 'POST':
        fm = CreateUser(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "User Created Successfully")
            return redirect("signup")
        else:
            messages.add_message(request, level=50, message="Please Fix The errors below", extra_tags="danger")
    else:
        fm = CreateUser()
    context = {"form": fm}
    return render(request, 'signup.html', context)


def signin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = LogUser(request, data=request.POST)
            if fm.is_valid():
                user = authenticate(request, username=fm.cleaned_data['username'], password=fm.cleaned_data['password'])
                if user is not None:
                    messages.success(request, "Successfully Logged In")
                    login(request=request, user=user)
                    return redirect("dashboard")

        else:
            fm = LogUser()
        context = {"form": fm}
        return render(request, 'signin.html', context)
    else:
        return redirect("dashboard")


def signout(request):
    logout(request)
    return redirect("signin")


def dashboard(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.all()
        context = {"blogs": blogs}
        print(request.user.user_permissions)
        return render(request, 'dashboard.html', context)
    else:
        return redirect('signin')


def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = BlogForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, "New Post Successfully Created")
                return redirect("dashboard")
        else:
            fm = BlogForm()
        context = {"form": fm}
        return render(request, 'addpost.html', context)
    else:
        return redirect("signin")


def edit_post(request, id):
    if request.user.is_authenticated:
        blogs = Blog.objects.get(pk=id)
        if request.method == "POST":
            fm = BlogForm(instance=blogs, data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, "Successfully Edited The Post")
                return redirect("dashboard")
        else:
            fm = BlogForm(instance=blogs)
        context = {"form": fm}
        return render(request, 'editpost.html', context)
    else:
        return redirect("signin")


def delete_post(request, id):
    if request.user.is_authenticated:
        blogs = Blog.objects.get(pk=id)
        blogs.delete()
        messages.success(request, "Blog Successfully Deleted")
        return redirect("dashboard")
    else:
        return redirect("signin")
