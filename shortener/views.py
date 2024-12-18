from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

from .models import Shortener
from .serializers import ShortenerSerializer, ShortenerStatsSerializer
# Create your views here.

class ShortenViewset(viewsets.ModelViewSet):
    queryset = Shortener.objects.all()
    serializer_class = ShortenerSerializer
    lookup_field = 'short_code'
    lookup_url_kwarg = 'short_code'
    
    @action(detail=True, methods=['get'])
    def stats(self, request, short_code=None):
        shortener = Shortener.objects.get(short_code=short_code)
        serializer = ShortenerStatsSerializer(shortener)
        return Response(serializer.data)
    
class RedirectView(viewsets.ViewSet):
    
    def retrieve(self, request, short_code=None):
        shortener = Shortener.objects.get(short_code=short_code)
        if shortener:
            shortener.access_count += 1
            shortener.save()
            return redirect(shortener.url)
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    