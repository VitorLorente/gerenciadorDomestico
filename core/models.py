from django.db import models
from django.contrib.auth.models import User


CATEGORIA_CHOICES = (
    (1, 'Empréstimo'),
    (2, 'Pagamento de empréstimo'),
    (3, 'Alimentação'),
    (4, 'Diversão')
)


class Movimento(models.Model):
    data = models.DateField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.SmallIntegerField(choices=CATEGORIA_CHOICES)
    descricao = models.CharField(max_length=300)

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
