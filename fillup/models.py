
from django.db import models
from django.utils import timezone


class Student(models.Model):
    id_num = models.CharField(max_length=10)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    course = models.TextField()
    year = models.TextField()


    def __str__(self):
        return self.id_num
