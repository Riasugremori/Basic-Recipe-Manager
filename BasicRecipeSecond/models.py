from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=200)
    instructions = models.CharField(max_length=200)



    def __str__(self):
        return self.name
