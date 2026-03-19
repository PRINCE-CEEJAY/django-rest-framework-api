from django.urls import path
from api import views

urlpatterns = [
    path('create_note/', views.NoteListCreateView.as_view(), name='create_note')
]