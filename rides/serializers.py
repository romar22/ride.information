from rest_framework.serializers import ModelSerializer

from .models import Ride, RideEvent
from users.serializers import UserSerializer


class RideEventSerializer(ModelSerializer):

    class Meta:
        model = RideEvent
        fields = (
            'id_ride_event',
            'description',
            'created_at',
        )


class RideSerializer(ModelSerializer):

    class Meta:
        model = Ride
        fields = (
            'id_ride',
            'status',
            'id_rider',
            'id_driver',
            'pickup_latitude',
            'pickup_longitude',
            'dropoff_latitude',
            'dropoff_longitude',
            'pickup_time',
            'ride_events'
        )
    
    def to_representation(self, instance):
        resp = super().to_representation(instance)
        resp['ride_events'] = RideEventSerializer(instance.ride_events.all(), many=True).data
        resp['id_rider'] = UserSerializer(instance.id_rider).data
        resp['id_driver'] = UserSerializer(instance.id_driver).data

        return resp