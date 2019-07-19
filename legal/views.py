from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import (
    ClientSerializer
)
from .models import (
    Client
)


class ClientViewSet(viewsets.ViewSet):
    queryset = Client.objects.all()
    serializer = ClientSerializer()

    def create(self, request):
        request.data['initials'] = request.data['first_name'][0]+request.data['last_name'][0]
        serializer = ClientSerializer(data=request.data)
        return Response(request.data)