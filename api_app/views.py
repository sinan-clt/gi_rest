from django.shortcuts import render
from api_app.serializers import *
from api_app.models import *
from django.http import QueryDict

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
import datetime

# Create your views here.


# Create a new Note **
class addNote(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        title = request.data["title"]
        body = request.data["body"]
        ordinary_dict = {'title': title, 'body': body}
        query_dict = QueryDict('', mutable=True)
        query_dict.update(ordinary_dict)
        note_details = AddNoteSerializer(data=query_dict)
        if note_details.is_valid():
            note_details.save()
            data = {'status': 200, "message": "note added successfully",
                    "data": note_details.data}
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {'status': 400, "message": "can't add note", "error": note_details.errors}
            return Response(data, status=status.HTTP_200_OK)



# List all Notes (will not show the deleted notes) **
class listNotes(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        note_details = Notes.objects.filter(is_available=True, is_deleted=False)
        serializer = ListNoteSerializer(note_details, many=True)
        data = {'status': 200, "message": "success", "data": serializer.data}
        return Response(data, status=status.HTTP_200_OK)


# Get single Note with primary key id **
class noteById(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        note_detail = Notes.objects.get(id=id)
        serializer = ListNoteSerializer(note_detail)
        data = {'status': 200, "message": "success", "data": serializer.data}
        return Response(data, status=status.HTTP_200_OK)



# Update Note with data provided in request **
class updateNote(APIView):
    permission_classes = [AllowAny]

    def put(self, request, id): 
        note = Notes.objects.get(id=id)
        serializer = EditNoteSerializer(note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        data = {'status': 200, "message": "note updated successfully","edited_data": serializer.data}
        return Response(data, status=status.HTTP_200_OK)


# Delete single Note with primary key id **
class deleteNote(APIView):
    permission_classes = [AllowAny]

    def delete(self, request, id):
        note = Notes.objects.filter(id=id).exists()
        if note is True:
            note = Notes.objects.get(id=id)
            note.is_deleted = True
            note.deleted_at = datetime.datetime.now()
            note.save()
            data = {'status': 400, "message": "note deleted successfully"}
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {'status': 400, "message": "note doesn't exist"}
            return Response(data, status=status.HTTP_200_OK)

