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
    
]
