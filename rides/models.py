from django.db import models

class Ride(models.Model):
    EN_ROUTE = 'en-route'
    PICKUP = 'pickup'
    DROPOFF = 'dropoff'
    STATUSES = (
        (EN_ROUTE, 'En-route'),
        (PICKUP, 'Pickup'),
        (DROPOFF, 'Dropoff')
    )

    id_ride = models.AutoField(primary_key=True)
    status = models.CharField(max_length=10, choices=STATUSES, default=EN_ROUTE)
    id_rider = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="ride_riders")
    id_driver = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="ride_drivers")
    pickup_latitude = models.FloatField()
    pickup_longitude = models.FloatField()
    dropoff_latitude = models.FloatField()
    dropoff_longitude = models.FloatField()
    pickup_time = models.DateTimeField()

    def __str__(self):
        return f"{self.id_ride}"


class RideEvent(models.Model):
    id_ride_event = models.AutoField(primary_key=True)
    id_ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name="ride_events")
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id_event}"