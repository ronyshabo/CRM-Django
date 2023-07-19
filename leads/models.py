from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
# To see the User Model Check the Abstract User model up here
# Recommended to create your own User model instead of the one provided by django

class User(AbstractUser):
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)
    def __str__(self):
        """
        This function helps the Query set of the User to returns the value of 
       information about them 
        """
        return (f" -{self.username}, - FN: {self.first_name}, -LN: {self.last_name}")
    # In the future if you wnat to add a new model to the db:
    # cellphone_number = models.CharField(max_length=15) 
    #migrate and that would be it

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
class Lead(models.Model):
# A representation of db schemas
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey("Category",null=True, blank=True, on_delete=models.SET_NULL )
        # if the agent is deleted we will delete the lead.
        # agent = models.ForeignKey("Agent", on_delete=models.SET_NULL)
        # this only works if Null is available
        # agent = models.ForeignKey("Agent", on_delete=models.SET_DEFAULT, default = "Something")
        # have a default value for that field
        # we have the forign key with leads allows the one to many relationship. 
        # where its hard to have an agent for each lead
    def __str__(self):
        """
        This function helps the Query set of the Agent to returns the value of 
        first and last name instead of just id number 
        """
        return f"{self.first_name} {self.last_name}"  



class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        """
        This function helps the Query set of the Agent to returns the value of 
        Email address rather than id number 
        """
        return f"{self.user.username} first name: {self.user.first_name} last name: {self.user.last_name}"

class Category(models.Model):
    name = models.CharField(max_length=30) #eg: new, contacted, converted "to sales", un converted
    organisation = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

#Signals will allow for events to listedn to other events and allow specific things to happen such as. 
def post_user_created_signal(sender, instance, created, **kwargs):
    """
    This function will return the 'sender of the event',
    'the instance' that is -ray8reaper, - FN: Rony, -LN: Shabo in our example
    'created' is the flag/marker that something was sent to the db. 
    """
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal,sender=User)