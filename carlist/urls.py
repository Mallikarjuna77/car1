from django.contrib import admin
from django.urls import path
from .views import Home,Search, Showroom, edit
urlpatterns = [
    path('admin/', admin.site.urls),
    path("edit/<str:Name>/", edit),
    path('search/<str:CarName>/', Search),
    path('home/', Home),
    path('showroom/<str:Name>/', Showroom),
]