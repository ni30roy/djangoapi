from django.db import models

# Create your models here.
class Courses(models.Model):
    name=models.CharField(max_length=200)
    lang=models.CharField(max_length=100)
    price=models.CharField(max_length=10)

    def __str__(self):
        return self.name
