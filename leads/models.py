from django.db import models
from django.contrib.auth.models import AbstractUser
# To see the User Model Check the Abstract User model up here
# Recommended to create your own User model instead of the one provided by django

class User(AbstractUser):
    def __str__(self):
        """
        This function helps the Query set of the User to returns the value of 
       information about them 
        """
        return (f" -{self.username}, - FN: {self.first_name}, -LN: {self.last_name}")
    # In the future if you wnat to add a new model to the db:
    # cellphone_number = models.CharField(max_length=15) 
    #migrate and that would be it

class Lead(models.Model):
# A representation of db schemas
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
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

    def __str__(self):
        """
        This function helps the Query set of the Agent to returns the value of 
        Email address rather than id number 
        """
        return f"{self.user.username} first name: {self.user.first_name} last name: {self.user.last_name}"

    