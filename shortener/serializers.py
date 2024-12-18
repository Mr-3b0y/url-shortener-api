from rest_framework import serializers

from .models import Shortener


class ShortenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        # fields = '__all__'
        exclude = ['access_count']
        read_only_fields = ['short_code', 'access_count']
        
class ShortenerStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        fields = '__all__'
        read_only_fields = ['url', 'short_code', 'created_at', 'updated_at']
        