from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Venue(models.Model):
    name = models.CharField('venue name',max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50,blank=True)
    zip_code = models.CharField(max_length=10,blank=True)
    phone = models.CharField(max_length=20,blank=True)
    website = models.URLField(max_length=200,blank=True)
    email = models.EmailField(max_length=254,blank=True)
    owner = models.IntegerField("Venue Owner", blank=False, default=1)
    venue_image = models.ImageField(null=True,blank=True,upload_to="images/")

    def __str__(self):
        return self.name
    
class MyClubUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return self.first_name+' '+self.last_name 
    
class Event(models.Model):
    name = models.CharField('event title',max_length=200)
    description = models.TextField(blank=True,null=True)
    manager = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    event_date = models.DateField("event date")
    venue = models.ForeignKey(Venue,blank=True,null=True, on_delete=models.CASCADE)
    attendees = models.ManyToManyField(MyClubUser, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def Daystill(self):
        import datetime
        daystillstripped = str(self.event_date - datetime.date.today()).split(",", 1)[0]
        return daystillstripped

    
    