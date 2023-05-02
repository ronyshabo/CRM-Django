https://www.youtube.com/watch?v=fOukA4Qh9QA

21:33 strating theory about django

after starting the venv 
"""
`source venv/scripts/activate

installed django

and started the project 
"""
`django-admnin startproject <Project Name>

"""
`python manage.py runserver



always remember, when you want to start working on django, yopu have to start an app, containerized module of code.
responsible for a single aspect of the project. 
eg: user, billing, such

to start using apps
"""
`python manage.py startapp <name> 

this creates a new directory and to be recognized as an apps
after any changes in the modles use 
"""
`python manage.py makemigrations
 
 ----then very importantly migrate to the bd so it applies

 """
 `python manage.py migrate


# Example format of the models is as such

# after any changes in the modles use python manage.py makemigrations

# class lead(models.Model):
#     SOURCE_CHOICES = (
#         ('YT','Youtube'),
#         ('GG','Google'),
#         ('LI','LinkedIn')
#     )
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     age = models.IntegerField(default=0)
#     # boolean fields:
#     phoned = models.BooleanField(default=False)
#     # Source field:
#     source = models.CharField(choices=SOURCE_CHOICES,max_length=100)
#     #Extra files
#     profile_picture = models.ImageField(blank=True, null=True)
#     special_files = models.FileField(blank=True, null=True)


