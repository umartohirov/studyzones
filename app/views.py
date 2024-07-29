from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth import login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import folium

from .decoraters import unauthenticated_user
from .models import Place,Location
from .forms import UserRegistrationForm



def home(request):
  place = Place.objects.all() 

  content = {
     'place':place
  }
  return render(request,'study/index.html',content)



def place(request,pk):
    place = Place.objects.get(id=pk)

    stuations = Location.objects.all()

    m = folium.Map(location=[41.5025,-72.699997],zoom_start=7)

    for station in stuations:
        coordinates = (station.lat, station.lng)
        folium.Marker(coordinates).add_to(m)

    content = {'map':m._repr_html_(),'place':place}

    return render(request,'study/place.html',content)


@unauthenticated_user
def register(request):
  form = UserRegistrationForm()

  if request.method == 'POST':
      form = UserRegistrationForm(request.POST)
      if form.is_valid():
          form.save()
          return redirect('login')  
  else:
      form = UserRegistrationForm()

  return render(request, 'study/register.html', {'form': form})

        


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'USERNAME OR PASSWORD IS INCORRECT')
    
    return render(request, 'study/login.html')


def logoutPage(request):
    logout(request)
    return redirect('login')



# MAP VIEWS
def locations_list(request):
    stuations = Location.objects.all()
    place = Place.objects.all()

    m = folium.Map(location=[41.3111, 69.2797],zoom_start=9)

    for station in stuations:
        coordinates = (station.lat, station.lng)
        folium.Marker(coordinates).add_to(m)

    

    content = {'map':m._repr_html_(),'places':place}
    return render(request,'study/locations.html',content)




