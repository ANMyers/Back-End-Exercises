from django.db import models

# Create your models here.
class HockeyTeam(models.Model):
	teamname = models.CharField(max_length=44)
	logo = models.FilePathField(path="/static/logos")
	city = models.CharField(max_length=255)
	coach = models.CharField(max_length=55)
	mascot = models.CharField(max_length=55)
	date = models.DateField()

	def __str__(self):
		return self.teamname

class HockeyPlayer(models.Model):
	playername = models.CharField(max_length=4)
	position = models.CharField(max_length=20)
	team = models.ForeignKey(HockeyTeam)

class Tornadoes(models.Model):
	classification = models.CharField(max_length=10)
	radius = models.CharField(max_length=25)
	color = models.CharField(max_length=25)
	speed = models.CharField(max_length=25)
	direction = models.CharField(max_length=50)
