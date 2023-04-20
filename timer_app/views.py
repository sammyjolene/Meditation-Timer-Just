from django.shortcuts import render, redirect
from django.urls import reverse 
from .models import Timer
from .forms import CustomTimer

# Create your views here.
def home(request):
    #add form with two places to input a number
    form = CustomTimer()
    if request.method == "POST":
        form = CustomTimer(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("home"))
    return render(request, "timer_app/home.html", {"form":form})
