from rest_framework import serializers
from api_app.models import *



class AddNoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notes
        fields = ['id', 'title', 'body']



class ListNoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notes
        fields = ('id','title','body','is_available','created_date','is_deleted')




class EditNoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notes
        fields = ['id', 'title', 'body']