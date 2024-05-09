from django.shortcuts import render, HttpResponse
import datetime
# Create your views here.
def index(request):
    # return HttpResponse("Weather Man")
    current_datetime = datetime.datetime.now()
    return render(request, 'index.html' ,{'current_datetime': current_datetime})