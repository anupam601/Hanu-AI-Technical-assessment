from django.urls import path
from .views import LocationGeoJSON, LocationStats

urlpatterns = [
    path('geojson/', LocationGeoJSON.as_view()),
    path('stats/', LocationStats.as_view()),
]
