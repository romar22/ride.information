from django.urls import path
from rides.views import Ride

urlpatterns = [
    path('', Ride.as_view({
        'get': 'list',
    }), name='rides'),
]