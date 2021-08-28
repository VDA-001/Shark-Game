from .models import SharkInfo
from .serializers import SharkListSerializer
from rest_framework import viewsets

# Create your views here.
class SharkViewSet(viewsets.ModelViewSet):
    queryset = SharkInfo.objects.all()
    serializer_class = SharkListSerializer