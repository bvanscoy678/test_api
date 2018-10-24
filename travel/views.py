#from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
#from django.db.models import Sum
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status
#from .serializers import CustomerSerializer
import datetime
import requests

now = timezone.now()


def home(request):
   return render(request, 'travel/home.html',
                 {'travel': home})


def search(request):
    city_from = request.POST.get("city_from", None)
    city_to = request.POST.get("city_to", None)
    departure = request.POST.get("departure", None)
    returning = request.POST.get("returning", None)
    adult = request.POST.get("adult", None)
    children = request.POST.get("children", None)

    if not (city_from and city_to and departure):
        return

    url = 'https://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?apikey=0FcV8cuF3wF2hQAbEeiEvLyFHrL4mj1H&number_of_results=5' + '&departure_date=' + departure
    if returning:
        url += '&return_date=' + returning
    if adult:
        url += '&adults=' + adult
    if children:
        url += '&children=' + children

    depart_url = url + '&origin=' + city_from + '&destination=' + city_to
    return_url = url + '&origin=' + city_to + '&destination=' + city_from

    depart_response = requests.get(depart_url)
    if depart_response.status_code == 200:
        depart_response = depart_response.json()

    return_response = requests.get(return_url)
    if return_response.status_code == 200:
        return_response = return_response.json()

    return render(request, 'travel/roundtrip.html',
                 {'depart_response': depart_response, 'return_response': return_response} )


def trip_request_new(request):
    if request.method == "POST":
        form = TripRequestForm(request.POST)
        if form.is_valid():
            trip_request = form.save(commit=False)
            trip_request.save()
            trip = trip_request.id
            #return render(request, 'travel/home.html')
            return render(request, 'travel/dept_iata_list.html')
    else:
        form = TripRequestForm()
        return render(request, 'travel/trip_request_new.html', {'form': form})


def trip_req_dept_city(request, pk):
    trip = get_object_or_404(TripRequest, pk=pk)
    city = trip.trip_dept_city
    main_api = 'https://api.sandbox.amadeus.com/v1.2/airports/autocomplete?apikey='
    api_key = '0FcV8cuF3wF2hQAbEeiEvLyFHrL4mj1H&term='
    url = main_api + api_key + city
    json_data = requests.get(url).json()
    city_list = []
    iata_list = []
    i = 0
    while True:
        city = (json_data[i]["label"])
        city_list.append(city)
        iata = (json_data[i]["value"])
        iata_list.append(iata)
        i = i + 1
        if (i > 1):
            break
    return render(request, 'travel/dept_iata_list.html', {'trip': trip,
                                                          'city': city,
                                                          'city_list': city_list,
                                                          'iata_list': iata_list})


