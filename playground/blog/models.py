from django.conf import settings
from django.db import models
from django.utils import timezone
 
class Equipement(models.Model):
    id_equip = models.CharField(max_length=100, primary_key=True)
    disponibilite = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)
    def __str__(self):
        return self.id_equip
 
  
class Membres(models.Model):
    id_membre = models.CharField(max_length=100, primary_key=True)
    etat = models.CharField(max_length=20)
    lateralite = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)
    lieu = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    def __str__(self):
        return self.id_membre

    
