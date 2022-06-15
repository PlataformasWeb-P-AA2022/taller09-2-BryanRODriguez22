from django.db import models
from requests import delete

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    siglas = models.CharField(max_length=5)
    twiiter = models.CharField(max_length=30) 

    def __str__(self):
        return "%s - %s - %s - " % (self.nombre, 
                self.siglas,
                self.twiiter)


class Jugador(models.Model):
    nombre = models.CharField(max_length=50)
    posicion = models.CharField(max_length=5)
    numero = models.IntegerField()
    sueldo = models.IntegerField()
    equipofut = models.ForeignKey(Equipo, related_name= 'losequipos',
        on_delete= models.CASCADE)

    def __str__(self):
        return "%s - %s - %d - %d -%s" % (self.nombre, 
            self.posicion,
            self.numero,
            self.sueldo,
            self.equipofut)

class Campeonato(models.Model):
    nombre = models.CharField(max_length=50)
    auspicia = models.CharField(max_length=50)

    def __str__(self):
        return "%s - %s" % (self.nombre,
        self.auspicia)

class CampeonatoEquipo(models.Model):
    anio = models.IntegerField()
    equipo_de_fut = models.ForeignKey(Equipo, related_name= 'loscampeonatos',
        on_delete= models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, related_name= 'loscampeonatos',
        on_delete= models.CASCADE)

    def __str__(self):
        return "Ficha: %s - Equipo(%s) - Campeonato(%s)" % (
            self.anio,
            self.equipo_de_fut.nombre,
            self.campeonato.nombre)
