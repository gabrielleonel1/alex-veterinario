from django.db import models
import uuid
from django_extensions.db.models import TimeStampedModel

from animal.models import AnimalModel

class HistoricoModel(TimeStampedModel):
    id = models.UUIDField(
        db_column="ID",
        primary_key=True,
        editable=False,
        unique=True,
        default= uuid.uuid4
    )

    animal_id = models.ForeignKey(
        AnimalModel,
        on_delete=models.CASCADE
    )

    data_entrada = models.DateField(auto_now=True)

    funcionario = models.CharField(max_length=50)

    tipo = models.CharField(max_length=20)

    descricao = models.TextField()


    def __str__(self) -> str:
        return self.id

    class Meta:
        db_table = 'HISTORICO'
        verbose_name = 'Historico'
        verbose_name_plural = 'Historicos'
