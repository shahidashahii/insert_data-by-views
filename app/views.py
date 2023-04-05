from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insert_topic(request):
    TN=input('enter topic name')
    TO=Topic.objects.get_or_create(topic_name=TN)[0]
    TO1.save()
    return HttpResponse('topic name is inserted')

def insert_webpage(request):
    N=input('enter name')
    URL=input('enter url')
    TO=Topic.objects.get_or_create(topic_name='Cricket')[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=N,url='URL')[0]
    WO.save()
    return HttpResponse('webpage data is inserted')

def insert_AccessRecord(request):
    author=input('enter author name')
    date=input('enter date')
    WO=Webpage.objects.get_or_create(name='Dhoni')[0]
    WO.save()
    AO=AccessRecord.objects.get_or_create(name=WO,author=author,date=date)[0]
    AO.save()
    return HttpResponse('access records are inserted')



