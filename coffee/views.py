from rest_framework.viewsets import ModelViewSet

from .models import Cafe, Avaliacao
from .serializers import CafeSerializer, AvaliacaoSerializer


class CafeViewSet(ModelViewSet):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer


class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer