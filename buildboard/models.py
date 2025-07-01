from django.db import models

COLORS = (('red','red'),('yellow','yellow'),('orange','orange'),('blue','blue'))

class Student(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=6, choices=COLORS)

    def __str__(self):
        return f'{self.name} : {self.color}'

