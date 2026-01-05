from django.db import models

class demomodel(models.Model):
    user_name=models.CharField(max_length=10)
    password=models.IntegerField()



# Create your models here.
