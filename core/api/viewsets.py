from rest_framework.viewsets import ModelViewSet
from core.models import Movimento
from .serializers import MovimentoSerializer


class MovimentoViewSet(ModelViewSet):
    queryset = Movimento.objects.all()
    serializer_class = MovimentoSerializer
