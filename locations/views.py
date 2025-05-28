from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Location
from django.db.models import Count

# GeoJSON view
class LocationGeoJSON(APIView):
    def get(self, request):
        locations = Location.objects.all()
        features = [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [loc.longitude, loc.latitude]
                },
                "properties": {
                    "name": loc.name,
                    "category": loc.category
                }
            }
            for loc in locations
        ]
        return Response({
            "type": "FeatureCollection",
            "features": features
        })

# Statistics view
class LocationStats(APIView):
    def get(self, request):
        total = Location.objects.count()
        top_category = Location.objects.values('category').annotate(count=Count('category')).order_by('-count').first()
        return Response({
            "total_locations": total,
            "most_common_category": top_category['category'] if top_category else None
        })
