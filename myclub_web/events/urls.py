from django.urls import path
from . import views
urlpatterns = [
    #int = numbers
    #str = strings
    #UUid = universal unique identifiers
    #path converters
    #slug = hyphens and underscores
    #path = urls
    path('date', views.home, name='date'),
    path('<int:year>/<str:month>/', views.home, 
         name='home', ),
    path('list_events', views.all_events, name='list_events'),
    path('add_venue', views.add_venue, name='add_venue'),
    path('add_event', views.add_event, name='add_event'),
    path('list_venue', views.list_venue, name='list-venue'),
    path('show_venue/<venue_id>', views.show_venue, name='show_venue'),

    path('update_venue/<venue_id>/',
        views.update_venue,
        name='update-venue'),

    path(
        'update_event/<int:event_id>/',
        views.update_event,
        name='update-event'
    ),    
    path('search_venues', views.search_venues, name='search-venues'),
    path('delete_venue/<venue_id>', views.delete_venue, name='delete-venue'),
    path('delete_event/<event_id>', views.delete_event, name='delete-event'),
    path('venue_text', views.venue_text, name='venue_text'),
    path('venue_csv', views.venue_csv, name='venue_csv'),
    path('venue_pdf', views.venue_pdf, name='venue_pdf'),

    
]
