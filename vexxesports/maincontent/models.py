from django.db import models
#from django.contrib.auth.models import User

#class UserProfile(models.Model):
#    user = models.OneToOneField(User)
#    is_player = models.BooleanField()

class Team(models.Model):
    team_name = models.CharField(max_length=100)
#    team = models.ManyToManyField(UserProfile)

    def __unicode__(self):
        return self.team_name

class Stream(models.Model):
    GAME_CHOICES = (
        ('all', 'All'),
        ('dota2', 'Dota2'),
        ('lol', 'League of Legends'),
        ('smite', 'Smite'),
        ('firefall', 'Firefall'),
    )
    stream_title = models.CharField(max_length=100)
    channel_name = models.CharField(max_length=100)
    game = models.CharField(max_length=100, choices=GAME_CHOICES)
#    player = models.ForeignKey(UserProfile)

    def __unicode__(self):
        return self.stream_title

class Guide(models.Model):
    guide_title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.guide_title