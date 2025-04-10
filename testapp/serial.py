from rest_framework import serializers
from .models import *

class dataserial(serializers.ModelSerializer):
    class Meta:
        model=allData
        fields='__all__'
        
class orderserial(serializers.ModelSerializer):
    class Meta:
        model=order
        fields='__all__'
                