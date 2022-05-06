import email
from django.db import models


class Curso(models.Model):      #Para que el modelo este en la base de datos
    nombre= models.CharField(max_length=50) #Es un char
    comision=models.IntegerField()  #Es un entero

class Estudiante(models.Model):
     nombre= models.CharField(max_length=50) #Es un char
     apellido=models.CharField(max_length=50)
     email= models.EmailField() 

class Profesor(models.Model):
     nombre= models.CharField(max_length=50) #Es un char
     apellido=models.CharField(max_length=50)
     email= models.EmailField() 
     profesion= models.CharField(max_length=50)

class Entregable(models.Model):
     nombre= models.CharField(max_length=50) #Es un char
     fecha_entrega=models.DateField()
     entregado= models.BooleanField()


#Make Migrations convierte todo este modelo en lenguaje SQL para guardarlo en una ba
#se de datos, es como commitear en git





# Create your models here.
