from django.urls import path
from api import views

urlpatterns = [
    path('note_list_create/', views.NoteListCreateView.as_view(), name='note_list_create'),
    path('notes/<int:pk>', views.NoteRetriveUpdateDestroyView.as_view(), name='update')
]