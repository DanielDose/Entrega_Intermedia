from django.db import models

# Create your models here.
class Empresa(models.Model):

    nombre_empresa=models.CharField(max_length=40)
    
    def __str__(self):
        return f"Empresa: {self.nombre_empresa}"

class Area(models.Model):
    nombre_area= models.CharField(max_length=30)
    cantidad_empleados= models.IntegerField()

class Trabajador(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)

# con esta indicación comenzamos a ver detalladamente en nuestra BD
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Profesión {self.profesion}"
