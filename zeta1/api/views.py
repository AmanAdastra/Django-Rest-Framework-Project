from django.shortcuts import render
from .models import Quotes
from .serializer import QuotesSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request,'api/home.html')  


def quoteget(request):
    q = Quotes.objects.all()
    serilizer = QuotesSerializer(q,many=True)
    json_data =JSONRenderer().render(serilizer.data)
    return HttpResponse(json_data,content_type='application/json')