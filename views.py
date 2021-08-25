from django.shortcuts import render
from django.http import HttpResponse
import pyttsx3
import pymongo
def EntryD(request):
    return render(request,'Form.html',{'head':'I Nominate as a Candidate for a Election of the Legislative Assembly of Chennai from the'})
def Way(request):
    ACname=str(request.GET['ACname'])
    PP=str(request.GET['PP'])
    Cname=str(request.GET['Cname'])
    Fname = str(request.GET['Fname'])
    CNum = int(request.GET['CNum'])
    Buss=str(request.GET['Buss'])
    mobli=int(request.GET['mobli'])
    PA = str(request.GET['PA'])
    state=str(request.GET['state'])
    distric=str(request.GET['distric'])
    posi=str(request.GET['posi'])
    incom=int(request.GET['incom'])
    # Date=int(request.GET['Date'])
    return render(request,'Form.html',{'ACname':ACname,'PP':PP,'Cname':Cname,'Fname':Fname,'CNum':CNum,'Buss':Buss,'mobli':mobli,
        'PA':PA,'state':state,'distric':distric,'posi':posi,'incom':incom})
def Final(request):
    ACname = str(request.GET['ACname'])
    PP = str(request.GET['PP'])
    Cname = str(request.GET['Cname'])
    Fname = str(request.GET['Fname'])
    CNum = int(request.GET['CNum'])
    Buss = str(request.GET['Buss'])
    mobli = int(request.GET['mobli'])
    PA = str(request.GET['PA'])
    state = str(request.GET['state'])
    distric = str(request.GET['distric'])
    posi = str(request.GET['posi'])
    incom = int(request.GET['incom'])
    # Date = int(request.GET['Date'])
    c=pymongo.MongoClient()
    db=c["database"]
    col=db["Election"]
    x=col.insert_one({'ACname':ACname,'PP':PP,'Cname':Cname,'Fname':Fname,'CNum':CNum,'Buss':Buss,'mobli':mobli,
                                        'PA': PA,'state':state,'distric':distric,'posi':posi,'incom':incom})
    return render(request,'Final.html',{'ACname':ACname,'PP':PP,'Cname':Cname,'Fname':Fname,'CNum':CNum,'Buss':Buss,'mobli':mobli,
                                        'PA': PA,'state':state,'distric':distric,'posi':posi,'incom':incom})
def index(request):
    speaker = pyttsx3.init()
    a=speaker.say('WELCOM TO  the  NOMINATION of Election to the TamilNadu Legislative Assembly')
    speaker.runAndWait()
    return render(request,'Index.html',{'Welcom':a})
def End(request):
    c = pymongo.MongoClient()
    db = c["database"]
    col = db["Election"]
    x=col.find()
    return render(request,'End.html',{'register': x})