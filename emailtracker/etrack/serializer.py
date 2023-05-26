from rest_framework import serializers
from .models import emailData
class emailSerializer(serializers.Serializer):
    email=serializers.EmailField()
    subject=serializers.CharField(max_length=100)
    body=serializers.CharField(max_length=500)

class postData(serializers.Serializer):
    class Meta:
        model = emailData
        fields = ['receiver', 'subject', 'receiver']

        def create(self, validated_data):
            instance = self.Meta.model(**validated_data)
            instance.save()
            return instance
    