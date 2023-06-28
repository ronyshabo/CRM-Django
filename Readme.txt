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



always remember, when you want to start working on django, you have to start an app, containerized module of code.
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

# after any changes in the modles use 
`python manage.py makemigrations

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

then 
`python manage.py migrate

VIMP : important section. python shell at 01:32:00

$ python manage.py createsuperuser
Username: ray8reaper
Email address: ray8reaper@gmail.com
Password: Boy from hell with money
Password (again):
Superuser created successfully.


today ended at 5:18:39 @ the beginning of agent detail
check on why agent page not showing agents.


