from rest_framework import serializers

class QuotesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    quote=serializers.CharField(max_length=100)
    author= serializers.CharField(max_length=50)