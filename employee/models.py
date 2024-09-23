from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()
    description = models.TextField(max_length=200)
    employee = models.ForeignKey("Employee", related_name='positionEmployee', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
