from django.urls import path
from . import views
urlpatterns = [
    #int = numbers
    #str = strings
    #UUid = universal unique identifiers
    #path converters
    #slug = hyphens and underscores
    #path = urls
    path('', views.home, name='home'),
    path('<int:year>/<str:month>/', views.home, 
         name='home',
         ),
    path('events/', views.all_events, name='list_events'),
    path('add_venue', views.add_venue, name='add_venue'),
    path('list_venue', views.list_venue, name='list-venue'),
    path('venue_show/<venue_id>', views.show_venue, name='show_venue'),
    
]
