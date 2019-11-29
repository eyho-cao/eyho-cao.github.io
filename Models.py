from django.db import models

#Creating the models
class Contract(models.Model):
    name = models.CharField(max_length=200)
    doorNo = models.SlugField(max_length=200)
    Address = models.TextField(black=True)
