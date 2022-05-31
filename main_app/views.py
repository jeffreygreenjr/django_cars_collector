from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
#...
from django.views.generic.base import TemplateView

from .models import Car

# Create your views here.

# Here we will be creating a class called Home and extending it from the Template View class
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"


 #adds artist class for mock database data
# class Car:
#     def __init__(self, name, year, image):
#         self.name = name
#         self.year = year
#         self.image = image

# cars = [
#     Car("Gorillaz", 
#         "2022",
#         "https://i.scdn.co/image/ab67616d00001e0295cf976d9ab7320469a00a29"),
#     Car("Panic! At The Disco",
#         "2003",
#         "https://i.scdn.co/image/58518a04cdd1f20a24cf0545838f3a7b775f8080"),
#     Car("Joji", 
#         "2020", 
#         "https://i.scdn.co/image/7bc3bb57c6977b18d8afe7d02adaeed4c31810df"),
# ]

class CarList(TemplateView):
    template_name = "car_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cars"] = Car.objects.all() # this is where we add the key into our context object for the view to use
        return context
