

# Create your models here.
from django.db import models
from django.contrib.auth.models import User



class Signup(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username



class Post(models.Model):

    title = models.CharField(max_length=200)

    content = models.TextField()

    def __str__(self):
        return self.title






class Theory(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)