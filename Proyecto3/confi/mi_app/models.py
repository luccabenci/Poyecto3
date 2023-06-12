from django.db import models

class Clase1(models.Model):
    campo1 = models.CharField(max_length=50)
    campo2 = models.IntegerField()

    class Meta:
        app_label = 'mi_app'

class Clase2(models.Model):
    campo3 = models.CharField(max_length=50)
    campo4 = models.IntegerField()

    class Meta:
        app_label = 'mi_app'
class Clase3(models.Model):
    campo5 = models.CharField(max_length=50)
    campo6 = models.IntegerField()

    class Meta:
        app_label = 'mi_app'