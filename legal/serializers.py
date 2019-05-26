from rest_framework import serializers
from .models import *

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('__all__')