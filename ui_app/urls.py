from django.urls import path
from . import views


urlpatterns = [

    path('ui_note/', views.notesUI, name="notesUI"),
    path('add_note/', views.addNote, name="add_note"),
    path('viewnotedata/<int:id>', views.noteData, name="viewnotedata"),
    path('note_edit_data/<int:id>', views.noteEditdata, name="noteEditdata"),
    path('editnote/<int:id>', views.editnote, name="editnote"),
    path('deletenote/<int:id>', views.deletenote, name="deletenote"),

]