from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('cars/', views.CarList.as_view(), name="car_list"),
    path('cars/new/', views.CarCreate.as_view(), name="artist_create")
]