from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response

from users.serializers import LoginSerializer


class Login(GenericViewSet):
    """ API Endpoint for user authentication
    """
    authentication_class = ()
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def authenticate(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(data=serializer.validated_data, status=HTTP_200_OK)
