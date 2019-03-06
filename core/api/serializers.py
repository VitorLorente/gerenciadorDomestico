from rest_framework.serializers import ModelSerializer
from core.models import Movimento


class MovimentoSerializer(ModelSerializer):
    class Meta:
        model = Movimento
        fields = ('id', 'data', 'valor', 'descricao', 'categoria', 'usuario')
