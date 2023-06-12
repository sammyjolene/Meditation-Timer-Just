from django.shortcuts import render, redirect
from django.urls import reverse 
from .models import Timer
from .forms import CustomTimer
from timer import timer

# Create your views here.
def home(request):
    #add form with two places to input a number
    form = CustomTimer()
    if request.method == "POST":
        form = CustomTimer(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("home"))
    #pull the most recent entry from the form for the two questions and import them into the timer.py function
    # meditation_length = 15
    # interval_length = 5
    #, "meditation_length":meditation_length, "interval_length":interval_length
    
    # countdown = timer(meditation_length, interval_length)"countdown": countdown
    return render(request, "timer_app/home.html", {"form":form})
