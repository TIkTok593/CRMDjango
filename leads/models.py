from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class User(AbstractUser):
    is_organizer = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.user.username


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    organization = models.ForeignKey(UserProfile, default=1, on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent", null=True, blank=True, default=None, on_delete=models.SET_DEFAULT)  # We surround the Agent with "", because Agent comes after Lead class, and python is a scripting language.
    category = models.ForeignKey("Category", related_name='leads', null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'{self.first_name} {self.second_name}'
    

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=30)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return self.name
    
    

def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:  # this is for users that have created before creating this signal
        if not UserProfile.objects.filter(user=instance):
            UserProfile.objects.create(user=instance)
            

post_save.connect(post_user_created_signal, sender=User)
