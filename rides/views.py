from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import (
    RideSerializer,
)
from .filters import (
    RideFilter
)
from .paginations import (
    RidePagination
)

class Ride(ModelViewSet):
    permission_classes = ()
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
        return self.serializer_class.Meta.model.objects.all()