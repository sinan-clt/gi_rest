from django.shortcuts import render,redirect
from api_app.models import *
import datetime


# Create your views here.
def notesUI(request):
    
    notes = Notes.objects.filter(is_deleted=False).order_by('-created_date')
    return render(request, 'note.html', {"note":notes})


def addNote(request):
    
    if request.method=='POST':
        title=request.POST['title']
        body=request.POST['body']
        note = Notes(title=title,body=body)
        note.save()
        return redirect('/ui_note/')
    return render(request,'addnote.html')


def noteData(request,id):
    
    single_note = Notes.objects.get(id=id)
    return render(request,'viewnote.html',{"note":single_note})


def noteEditdata(request,id):
    
    single_note=Notes.objects.get(id=id)
    return render(request,'editnoteview.html',{"note":single_note})


def editnote(request,id):
    
    if request.method == 'POST':
        note=Notes.objects.get(pk=id)
        note.title=request.POST['title']
        note.body=request.POST['body']
        note.save()
        return redirect('/ui_note/')
    else:
        return redirect('/ui_note/')
    
    
    
def deletenote(request, id):
    
    note = Notes.objects.get(id = id)
    note.is_deleted = True
    note.deleted_at = datetime.datetime.now()
    note.save()
    return redirect('/ui_note/')