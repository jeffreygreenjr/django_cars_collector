from django.urls import reverse

from django.shortcuts import render, redirect
from django.http import HttpResponse # <- a class to handle sending a type of response

from django.views import View # <- View class to handle requests
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView

# Auth
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Car

# Create your views here.

# Here we will be creating a class called Home and extending it from the Template View class
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"


class CarList(TemplateView):
    template_name = "car_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["cars"] = Car.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["cars"] = Car.objects.all()
            # default header for not searching 
            context["header"] = "Trending Cars"
        return context


@method_decorator(login_required, name='dispatch')
class MyCarList(TemplateView):
    template_name = "my_car_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["cars"] = Car.objects.filter(
                name__icontains=name, user=self.request.user)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["cars"] = Car.objects.filter(user=self.request.user)
            # default header for not searching 
            context["header"] = "Trending Cars"
        return context


class CarCreate(CreateView):
    model = Car
    fields = ['name', 'year', 'manufacturer', 'vehicletype', 'bio', 'img']
    template_name = "car_create.html"
     # This is our new method that will add the user into our submitted form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CarCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('car_detail', kwargs={'pk': self.object.pk})


class CarDetail(DetailView):
    model = Car
    template_name = "car_detail.html"


class CarUpdate(UpdateView):
    model = Car
    fields = ['name', 'year', 'manufacturer', 'vehicletype', 'bio', 'img']
    template_name = "car_update.html"
    def get_success_url(self):
        return reverse('car_detail', kwargs={'pk': self.object.pk})


class CarDelete(DeleteView):
    model = Car
    template_name = "car_delete_confirmation.html"
    success_url = "/cars/"


class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form ssubmit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("car_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
