from django.db import models
import uuid
from django_extensions.db.models import TimeStampedModel

from cliente.models import ClienteModel


class AnimalModel(TimeStampedModel): 
    id = models.UUIDField(
        db_column="ID",
        primary_key=True,
        editable=False,
        unique=True,
        default= uuid.uuid4
    )

    cliente_id = models.ForeignKey(
        ClienteModel,
        on_delete=models.DO_NOTHING
    )

    nome = models.CharField(
        db_column="NOME",
        max_length=30
    )

    raca = models.CharField(
        db_column="TIPO",
        max_length=20
    )

    sexo = models.CharField(
        db_column="SEXO",
        max_length=6
    )

    idade = models.CharField(
        db_column="IDADE",
        max_length=3
    )