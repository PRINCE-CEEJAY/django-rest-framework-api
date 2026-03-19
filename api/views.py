from rest_framework.generics import ListCreateAPIView
from api.models import Note
from rest_framework import generics
from api.serializers import ApiSerializer

class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = ApiSerializer
