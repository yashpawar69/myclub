from django.contrib import admin
from .models import Events
from .models import Venue
from .models import MyClubUser
# Register your models here.

admin.site.register(Events)
admin.site.register(Venue)
admin.site.register(MyClubUser)