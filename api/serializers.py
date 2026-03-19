from rest_framework import serializers
from api.models import Note

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'date_created']    