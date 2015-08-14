from django.db import models

class Cancha(models.Model):
	nombre = models.CharField(max_length=30)
	ubicacion = models.CharField(max_length=50)


class Reta(models.Model):
	horario = models.DateTimeField()
	cancha = models.ForeignKey('Cancha')


class Equipo(models.Model):
	nombre = models.CharField(max_length=30)
	max_jugadores = models.IntegerField(default=7)
	reta = models.ForeignKey('Reta')


class Jugador (models.Model):
	nombre = models.CharField(max_length=30)
	avatar = models.ImageField()
	equipo = models.ForeignKey('Equipo')

