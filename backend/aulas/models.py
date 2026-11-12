from django.db import models

class Carrera(models.Model):
    nombre = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.nombre


class Profesor(models.Model):
    nombre = models.CharField(max_length=128, null=False)
    apellido = models.CharField(max_length=128, null=False)
    mostrar = models.CharField(max_length=256, null=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Materia(models.Model):
    nombre = models.CharField(max_length=128, null=False)
    cant_alumnos = models.IntegerField(default=5, null=False)
    id_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, null=False)
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nombre


class Aula(models.Model):
    descripcion = models.CharField(max_length=128, null=False)
    ubicacion = models.CharField(max_length=128, null=False)
    cant_proyector = models.IntegerField(default=0)
    aforo = models.IntegerField(default=0)
    es_climatizada = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion