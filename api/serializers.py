from rest_framework import serializers
from .models import Customer,Order

class orderSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Order
        fields = ('__all__')

class customerSerializer(serializers.HyperlinkedModelSerializer):
    orders = orderSerializer(many=True,read_only=True)
    class Meta:
        model=Customer
        fields=('__all__')

class SocialSerializer(serializers.Serializer):
    provider = serializers.CharField(max_length=255, required=True)
    access_token = serializers.CharField(max_length=4096, required=True, trim_whitespace=True)


