from rest_framework import serializers


class ImageSerializer(serializers.Serializer):
    food_image = serializers.ImageField()
