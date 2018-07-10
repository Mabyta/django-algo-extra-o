#
import math

from django.db import models
#Se importa el modelo de usuarios que tiene django por default
from django.contrib.auth.models import User
#
from django.utils.html import mark_safe
#
from django.utils.text import Truncator
#Extension que agrega edicion de texto como negrita, cursiva, nivel de titulos, formato de lista, etc.
from markdown import markdown

class Roles(models.Model):
    nombre_rol = models.CharField(max_length=30)
    Usuario = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

