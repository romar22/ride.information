import factory
from factory.django import DjangoModelFactory
from faker import Faker
from rides.models import Ride, RideEvent
from django.utils import timezone
import pytz

fake = Faker()

class RideFactory(DjangoModelFactory):
    class Meta:
        model = Ride

    status = Ride.EN_ROUTE
    id_rider = factory.SubFactory('users.test.factories.UserFactory')
    id_driver = factory.SubFactory('users.test.factories.UserFactory')
    pickup_latitude = fake.latitude()
    pickup_longitude = fake.longitude()
    dropoff_latitude = fake.latitude()
    dropoff_longitude = fake.longitude()
    pickup_time = timezone.make_aware(fake.date_time_this_year(), timezone=pytz.UTC)


class RideEventFactory(DjangoModelFactory):
    class Meta:
        model = RideEvent

    id_ride = factory.SubFactory(RideFactory)
    description = fake.text()
    created_at = timezone.make_aware(fake.date_time_this_year(), timezone=pytz.UTC)
