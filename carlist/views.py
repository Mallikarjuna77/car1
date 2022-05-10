from django.shortcuts import render, redirect
from .forms import carlistForm, Show_roomForm
from .models import carlist, Show_room, CarModels

def Home(request):
    all_cars=carlist.objects.all()
    return render(request,"index.html",{"cars":all_cars})

def edit(request, CarName):
    data=carlist.objects.filter(CarName__icontains=CarName)
    return render(request, 'update.html', {'Name':data})

def Search(request, CarName):
    option=carlist.objects.filter(CarName__icontains=CarName)
    return render(request,"search.html",{"carrecord":option})

def Showroom(request, Name):
    caption=Show_room.objects.all(Name__icontains=Name)
    return render(request,"Showroom.html", {"record":caption})



    # hold=carlist.objects.filter(CarName__icontains=CarName)
    # return render(request, "search.html",{"carrecord":hold})


