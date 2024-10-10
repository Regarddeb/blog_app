from rest_framework import serializers

class BlogRequestSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()