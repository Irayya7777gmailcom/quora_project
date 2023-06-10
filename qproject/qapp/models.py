from django.db import models

# Create your models here.
class postq(models.Model):
    question=models.TextField()
    answers=models.TextField()
    likes=models.ManyToManyField('self',related_name='likess',symmetrical=False) 

class signup(models.Model):
    user=models.CharField(max_length=50)
    passwd=models.CharField(max_length=50)

class postqu(models.Model):
    question=models.TextField()
    answers=models.TextField()
    like=models.CharField(max_length=10)