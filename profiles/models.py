from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
    def __str__(self):
        return str(self.user)
    user = models.OneToOneField(User, related_name='user')
    use_2fa = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    xp = models.PositiveSmallIntegerField(default=0)
    credits = models.PositiveSmallIntegerField(default=0)
    total_earning = models.PositiveSmallIntegerField(default=0)
    about_me = models.CharField(max_length=500, default='', blank=True)
    xbl = models.CharField(max_length=15, default='', blank=True)
    psn = models.CharField(max_length=16, default='', blank=True)
    twitter_profile = models.CharField(max_length=15, default='', blank=True)
    twitch_channel = models.CharField(max_length=50, default='', blank=True)
    favorite_game = models.CharField(max_length=50, default='', blank=True)
    favorite_console = models.CharField(max_length=50, default='', blank=True)
    profile_picture = models.ImageField(upload_to='profile_images', blank=True)
    user_type = models.CharField(max_length=10, default='user')

#def create_profile(sender, **kwargs):
#    if kwargs['created']:
#        user_profile = UserProfile.objects.create(user=kwargs['instance'])
def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()

post_save.connect(create_profile, sender=User)
