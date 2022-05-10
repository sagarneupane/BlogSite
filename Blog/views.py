from django.shortcuts import render
from .forms import DummyForm


# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)


def contact(request):
    fm = DummyForm()
    context = {"form": fm}
    return render(request, 'contact.html', context)


def about(request):
    return render(request, 'about.html')
