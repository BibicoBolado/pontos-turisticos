from django.db import models

# Create your models here.

class Localizacao (models.Model):
    linha1=models.CharField(max_length=150)
    linha2=models.CharField(max_length=150,null=True,blank=True)
    cidade=models.CharField(max_length=150)
    estado=models.CharField(max_length=150)
    pais=models.CharField(max_length=150)
    lat=models.FloatField(null=True,blank=True)
    lon=models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.linha1