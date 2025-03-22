from django.db import models

# Create your models here.

class Trainee(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.name
