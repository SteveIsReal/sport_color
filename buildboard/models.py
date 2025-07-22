from django.db import models

STATUS = (('single','single'),('pair','pair'),('team','team'))
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
    status = models.CharField(max_length=6, choices=STATUS, null=True)

    def __str__(self):
        return f'{self.status} : {self.color} : {[i.name for i in self.members.all()]}'
