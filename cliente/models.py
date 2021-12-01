from django.db import models
import uuid
from django_extensions.db.models import TimeStampedModel

class ClienteModel(TimeStampedModel): 
    id = models.UUIDField(
        db_column="ID",
        primary_key=True,
        editable=False,
        unique=True,
        default= uuid.uuid4
    )

    nome = models.CharField(
        db_column="NOME",
        max_length=100
    )

    cpf = models.CharField(
        db_column="CPF",
        max_length=11,
        unique=True,
    )

    sexo = models.CharField(
        db_column="SEXO",
        max_length=7
    )


    telefone = models.CharField(
        db_column="TELEFONE",
        max_length=11
    )

    email = models.EmailField(
        db_column="EMAIL",
        max_length=150
    )