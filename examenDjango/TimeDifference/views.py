from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
import pytz

# Create your views here.

def index(request):
    
    dateNow = datetime.now()
    DateBrexit = datetime(2019,3,29,11)

    londen = pytz.timezone("Europe/London")
    dateNow = londen.localize(dateNow)
    DateBrexit = londen.localize(DateBrexit)

    diff = DateBrexit - dateNow

    days, seconds = diff.days, diff.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    total = hours,"h " ,minutes,"m " ,seconds, "s"


    return HttpResponse(total)