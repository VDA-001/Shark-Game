from rest_framework import serializers
from .models import SharkInfo

class SharkListSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None,allow_empty_file = False,allow_null = True,required = False)
    class Meta:
        model = SharkInfo
        fields = ('title','image','strength','speed','iq')