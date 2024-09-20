from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from datetime import date
from django.db.models import Prefetch
from users.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    RideSerializer,
    RideEventSerializer,
)
from .filters import (
    RideFilter
)
from .paginations import (
    RidePagination
)

class Ride(ModelViewSet):
    permission_classes = (IsAdmin, IsAuthenticated, )
    serializer_class = RideSerializer
    filterset_class = RideFilter
    pagination_class = RidePagination
    ordering_fields = (
        'pickup_time', 
        'pickup_latitude', 
        'pickup_longitude', 
        'dropoff_time', 
        'dropoff_latitude', 
        'dropoff_longitude'
    )
    ordering = ('pickup_time',)

    def get_queryset(self):
        RideEvent = RideEventSerializer.Meta.model
        return self.serializer_class.Meta.model.objects.all()\
            .select_related('id_rider', 'id_driver')\
            .prefetch_related(
                Prefetch('ride_events', queryset=RideEvent.objects.filter(created_at__date=date.today()))
            )