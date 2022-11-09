from django.urls import path
from . import views


urlpatterns = [



    path('add_note', views.addNote.as_view(), name="addNote"),
    path('list_notes', views.listNotes.as_view(), name="listNotes"),
    path('note_by_id/<int:id>', views.noteById.as_view(), name="noteById"),
    path('update_note/<int:id>', views.updateNote.as_view(), name="updateNote"),
    path('delete_note/<int:id>', views.deleteNote.as_view(), name="deleteNote"),



]