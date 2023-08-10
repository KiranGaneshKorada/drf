from rest_framework import serializers
from .models import Reservation,Passenger,Flight
import re

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flight
        fields='__all__'

    # INDIVIDUAL VALIDATION
    def validate_flightNumber(self,flightNumber):
        if(re.match("^[a-zA-Z0-9]*$",flightNumber)==None):
            raise serializers.ValidationError("Invalid Flight Number.Make sure to have alphanumeric")
        return flightNumber
    
    # ALL VALIDATION IN ONE FUNCTION
    #def validate(self,data):
    #    data['flightNumber']
    #    put all your if condition logic here one by one for every varialble using above logic


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Passenger
        fields='__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields='__all__'