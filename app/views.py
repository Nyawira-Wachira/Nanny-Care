from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from app.models import Nanny, Bio

# Create your views here.


def welcome(request):
    nanny = Nanny.objects.all()
    bio = Bio.objects.all()
    return render(request, 'nannydetails.html', {'nanny':nanny}, {'bio':bio})
