from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound

# Create your views here.

def index(request):
    
    dateNow = datetime.now().astimezone
    DateBrexit = datetime(2019,3,29,11)

    diff = DateBrexit - dateNow

    days, seconds = diff.days, diff.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    total = hours,"h " ,minutes,"m " ,seconds, "s"


    return HttpResponse(total)