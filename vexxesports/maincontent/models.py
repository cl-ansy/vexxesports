from django.db import models
#from django.contrib.auth.models import User

#class UserProfile(models.Model):
#    user = models.OneToOneField(User)
#    is_player = models.BooleanField()

class Team(models.Model):
    name = models.CharField(max_length=100)
#    team = models.ManyToManyField(UserProfile)

class Stream(models.Model):
    name = models.CharField(max_length=100)
    stream_url = models.CharField(max_length=100)
#    player = models.ForeignKey(UserProfile)

class Guide(models.Model):
    name = models.CharField(max_length=100)