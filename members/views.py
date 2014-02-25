import json
from django.http import HttpResponse
from .models import member,ministers
# Create your views here.

def home(request):
    members = member.objects.all().order_by('name')
    membersList = []

    for m in members:
        memberDict = {}
        memberDict['name']=m.name
        memberDict['photo']="http://app.labelag.com/"+m.photo.url
        memberDict['description']=m.description
        membersList.append(memberDict)


    return  HttpResponse(json.dumps(membersList), content_type="application/json")

def home2(request):
    members = ministers.objects.all().order_by('name')
    membersList = []

    for m in members:
        memberDict = {}
        memberDict['name']=m.name
        memberDict['photo']="http://app.labelag.com/"+m.photo.url
        memberDict['description']=m.description
        membersList.append(memberDict)


    return  HttpResponse(json.dumps(membersList), content_type="application/json")

