from django.db import models
from django.utils import timezone
import requests


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_arrival_date = models.DateField(default=timezone.now)
    hotel_dept_date = models.DateField(default=timezone.now)
    hotel_price = models.DecimalField(max_digits=10, decimal_places=2)


class Flight(models.Model):
    flight_airline = models.CharField(max_length=100)
    flight_dept_code = models.CharField(max_length=10)
    flight_dept_city = models.CharField(max_length=100)
    flight_dept_date = models.DateTimeField(default=timezone.now)
    flight_arrival_code = models.CharField(max_length=10)
    flight_arrival_city = models.CharField(max_length=100)
    flight_arrival_date = models.DateTimeField(default=timezone.now)
    flight_price = models.DecimalField(max_digits=10, decimal_places=2)


class Trip(models.Model):
    flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)


class TripRequest(models.Model):
    trip_dept_date = models.DateField(default=timezone.now)
    trip_dept_city = models.CharField(max_length=100)
    trip_dest_city = models.CharField(max_length=100)
    trip_ret_date = models.DateField(default=timezone.now)
    trip_dept_iata = models.CharField(max_length=5)
    trip_dest_iata = models.CharField(max_length=5)

    def iata_code(self):
        print("Got here")
        city = str(self.trip_dept_city)
        main_api = 'https://api.sandbox.amadeus.com/v1.2/airports/autocomplete?apikey='
        api_key = '0FcV8cuF3wF2hQAbEeiEvLyFHrL4mj1H&term='
        url = main_api + api_key + city
        json_data = requests.get(url).json()
        city_list = []
        #iata_list = []
        i = 0
        print("Got to while")
        while True:
            print("in loop" + str(i))
            city = (json_data[i]["label"])
            city_list.append(city)
            iata = (json_data[i]["value"])
            #iata_list.insert(i, iata)

            print("city: " + city + "   iata: " + iata)
            print(city_list[i])
            i = i + 1
            if(i > 1):
                break
        print("After loop   " + city_list[0])
        print(len(city_list))
        return city_list, #, iata_list
