from django.db import models
# mapeo  a las bases de datos 
# Create your models here.

  # poner atributos 
class contact(models.Model):
  nombre = models.CharField(max_length=30)
  telefono = models.CharField(max_length=30)
  correo = models.CharField(max_length=30)
  mensaje = models.TextField()


