from django.db import models


class Profesion(models.Model):
    nombre = models.CharField(max_length=64, verbose_name="Nombre")

    def __str__(self):
        return self.nombre


# Create your models here.
class AutorModel(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Nombre")
    fecha_nacimiento = models.DateField(verbose_name="Fecha Nacimiento", null=False, blank=False)
    fecha_fallecimiento = models.DateField(verbose_name="Fecha Fallecimiento", null=True, blank=True)
    profesion = models.ManyToManyField(Profesion, verbose_name="Profesion")
    nacionalidad = models.CharField(verbose_name="Nacionalidad", max_length=64)

    class Meta:
        db_table = "Autores"
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self) -> str:
        return self.nombre


class FraseModel(models.Model):
    cita = models.TextField(verbose_name="Cita", max_length=500)
    autor_fx = models.ForeignKey(AutorModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Frase"
        verbose_name_plural = "Frases"