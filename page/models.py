from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    time = models.DateTimeField()

class Student(models.Model):
    name = models.CharField(max_length=30)
    major = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.name