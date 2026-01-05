from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.CharField(max_length=100)
    dob = models.DateField()
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class reporter(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class article(models.Model):
    headline=models.CharField(max_length=100)
    pub_date=models.DateField()
    repoter=models.ForeignKey(reporter,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.headline

class Meta:
    ordering=["headline"]


class usermodel(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.username




# Create your models here.
