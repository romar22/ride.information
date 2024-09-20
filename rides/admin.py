from django.contrib import admin
from .models import Ride, RideEvent

@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ["id_ride", "status", "id_rider", "id_driver", "pickup_latitude", "pickup_longitude", "dropoff_latitude", "dropoff_longitude", "pickup_time"]

@admin.register(RideEvent)
class RideEventAdmin(admin.ModelAdmin):
    list_display = ["id_ride_event", "id_ride", "description", "created_at"]
