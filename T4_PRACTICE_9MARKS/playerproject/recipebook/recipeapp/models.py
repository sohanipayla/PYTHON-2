from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    cooking_time = models.IntegerField(help_text="Time in minutes")

    def __str__(self):
        return self.name
