import json
from django.http import HttpResponse
from .models import member
# Create your views here.

def home(request):
    members = member.objects.all()
    membersList = []

    for m in members:
        memberDict = {}
        memberDict['name']=m.name
        memberDict['photo']=m.photo.url
        if m.description:
            memberDict['description']=m.description
        membersList.append(memberDict)


    return  HttpResponse(json.dumps(membersList), content_type="application/json")
