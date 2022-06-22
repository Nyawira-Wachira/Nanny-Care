from django.shortcuts import render, redirect, get_object_or_404


from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

from .models import User, Nanny, Bio, UserProfile

# Create your views here.
def Index(request):


    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')

@login_required(login_url='/accounts/login/')
def profile(request, username):
    user = get_object_or_404(User, username=username)
    
    context = {
        'user': user
    }
    return render(request, 'profile/profile.html', context)



@login_required(login_url='/accounts/login/')
def booking(request):
    return render(request, 'book/booking.html')


def details(request):

    nanny = Nanny.objects.all()
    return render(request, 'nannydetails/nannydetails.html', {'nanny':nanny})


def companydetails(request):
    gallery = Nanny.objects.all() [:8]

    return render (request, 'companydetails/company_detail.html',{'gallery':gallery})
