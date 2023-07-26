from django.db import models


# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=200, null=False)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.IntegerField()

    class Meta:
        db_table = "student"
