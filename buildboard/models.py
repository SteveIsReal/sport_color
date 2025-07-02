from django.db import models

COLORS = (('red','red'),('yellow','yellow'),('orange','orange'),('blue','blue'))

class Game(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Student(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=6, choices=COLORS)

    def __str__(self):
        return f'{self.name} : {self.color}'

class Team(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=6, choices=COLORS)
    members = models.ManyToManyField(Student)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.members}'


