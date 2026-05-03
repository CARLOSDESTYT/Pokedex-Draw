from django.db import models

class Pokemon(models.Model):
    numero = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    tipos = models.CharField(max_length=40)
    img_path = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.numero} - {self.nombre}"