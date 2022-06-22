from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcome(request):
    gallery = Image.objects.all() [:8]

    return render (request, 'company_detail.html',{'gallery':gallery})
