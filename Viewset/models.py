from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=50,unique=True)
    roll=models.IntegerField(default=0)
    city=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
