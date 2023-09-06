from doctest import REPORT_ONLY_FIRST_FAILURE
from wsgiref.validate import validator
from flightApp.models import Flight,Passenger,Reservation
from rest_framework import serializers
import re



def validator_function(data):
    '''Write validation logic here and call in serializer class, gets all data'''
    return data


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        validators = [validator_function]
    
    def validate_flightNumber(self,flightNumber):
        if re.match('^[a-zA-Z0-9]*$',flightNumber) == None:
            raise serializers.ValidationError("Flight Number invalid, should be Alphanumeric")
        return flightNumber
    
    
    
    def validate(self, data):

        # Can write Validating Logic here for all fields

        print(data['flightNumber']) # gets all data from model

        return data


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

