from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Ride

class RidePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'