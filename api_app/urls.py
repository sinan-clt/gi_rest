from django.urls import path
from . import views


urlpatterns = [
    
    path('note', views.Note.as_view(), name="note"),
    path('note/<int:id>', views.noteCrud.as_view(), name="notecrud"),
    

]