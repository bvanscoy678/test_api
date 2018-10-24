from django.contrib import admin
from .models import Flight, Hotel, Trip, TripRequest

class FlightList(admin.ModelAdmin):
    list_display = ('flight_airline','flight_dept_code','flight_dept_city','flight_dept_date',
                    'flight_arrival_code','flight_arrival_city','flight_arrival_date','flight_price')
    list_filter = ('flight_airline','flight_dept_date')
    ordering = ['flight_dept_date']


class HotelList(admin.ModelAdmin):
    list_display = ('hotel_name','hotel_arrival_date','hotel_dept_date','hotel_price')
    ordering = ['hotel_arrival_date']


class TripList(admin.ModelAdmin):
    list_display = ('id','flight_id','hotel_id')


class TripRequestList(admin.ModelAdmin):
    list_display = ('trip_dept_date','trip_dept_city','trip_dest_city','trip_ret_date','trip_dept_iata','trip_dest_iata')


admin.site.register(Flight, FlightList)
admin.site.register(Hotel, HotelList)
admin.site.register(Trip, TripList)
admin.site.register(TripRequest, TripRequestList)
