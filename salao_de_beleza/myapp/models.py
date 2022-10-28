from dataclasses import fields
import email
from django.db import models

# Create your models here.

class Usuario(models.Model):
    usuario = models.CharField(max_length=16)
    senha = models.CharField(max_length=16)
    nome = models.CharField(max_length=16)
    ultimo_nome = models.CharField(max_length=16)

class Comentario(models.Model):
    comentario = models.TextField(max_length=255)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)




