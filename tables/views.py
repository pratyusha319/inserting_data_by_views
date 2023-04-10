from django.shortcuts import render

# Create your views here.
from tables.models import *
from django.http import HttpResponse

def  topics(request):
    T=input("enter a name :")
    To=Topic.objects.get_or_create(topic_name=T)[0]
    To.save()
    return HttpResponse('topic inserted successfully')
def  webpages(request):
    T=input("enter a name :")
    name=input("enter a name :")
    urls=input("enter a name :")
    To=Topic.objects.get_or_create(topic_name=T)[0]
    To.save()
    wo=Webpage.objects.get_or_create(topic_name=To,Web_name=name,url=urls)[0]
    wo.save()
    return HttpResponse('topic inserted successfully')
def accessrecords(request):
   
    name=input("enter a name :")
    a=input("enter author name :")
    d=input("enter date :")

    wo=Webpage.objects.get_or_create(Web_name=name)[0]
    wo.save()
    ao=AccessRecords.objects.get_or_create(Web_name=wo,author=a,date=d)[0]
    ao.save()
    return HttpResponse('topic inserted successfully')


