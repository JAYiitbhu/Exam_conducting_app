from django.db import models

# Create your models here.
class Comments(models.Model):
    studid =models.IntegerField()
    comments=models.TextField()
    teachid=models.IntegerField()



