from django import forms
from .models import TripRequest

class TripRequestForm(forms.ModelForm):
    class Meta:
        model = TripRequest
        fields = ('trip_dept_date','trip_dept_city','trip_dest_city','trip_ret_date',)
