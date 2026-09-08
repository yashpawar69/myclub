from django.db import models

# Create your models here.

class Venue(models.Model):
    name = models.CharField('venue name',max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name
    
class MyClubUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return self.first_name+' '+self.last_name 
    
class Events(models.Model):
    title = models.CharField('event title',max_length=200)
    description = models.TextField()
    host = models.CharField(max_length=50)
    date = models.DateField("event date")
    venue_object = models.ForeignKey(Venue,blank=True,null=True, on_delete=models.CASCADE)
    attendees = models.ManyToManyField(MyClubUser, blank=True)

    def __str__(self):
        return self.title
    