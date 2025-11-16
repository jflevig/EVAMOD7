from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    etiquetas = models.ManyToManyField(Etiqueta, related_name='productos')

    def __str__(self):
        return self.nombre

class Detalle(models.Model):
    color = models.CharField(max_length=100, blank=True)
    tamaño = models.CharField(max_length=100, blank=True)
    peso = models.CharField(max_length=100, blank=True)
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE, related_name='detalle')
    
