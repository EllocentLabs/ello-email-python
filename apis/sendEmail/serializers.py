from rest_framework import serializers
from rest_framework.fields import EmailField


class EmailSerializer(serializers.Serializer):
    email = EmailField()
