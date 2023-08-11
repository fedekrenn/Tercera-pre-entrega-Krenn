from django.db import models


# Create your models here.
class Receta(models.Model):
    nombre = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=200)
    tiempo = models.IntegerField()
    DIFICULTAD = (
        (1, "Fácil"),
        (2, "Media"),
        (3, "Difícil"),
    )
    dificultad = models.IntegerField(choices=DIFICULTAD)

    def __str__(self):
        return self.nombre


class Cocinero(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    especialidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + " " + self.apellido


class Restaurante(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    CATEGORIA = (
        ("Comida rápida", "Comida rápida"),
        ("Meriendas", "Meriendas"),
        ("Veggie", "Veggie"),
        ("Cena", "Cena"),
    )
    categoria = models.CharField(max_length=50, choices=CATEGORIA)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    PRODUCTO = (
        ("Carnes", "Carnes"),
        ("Verdura", "Verdura"),
        ("Bebidas", "Bebidas"),
        ("Pescado", "Pescado"),
        ("Postres", "Postres"),
        ("Pan", "Pan"),
    )
    producto = models.CharField(max_length=50, choices=PRODUCTO)

    def __str__(self):
        return self.nombre + " - " + self.producto
