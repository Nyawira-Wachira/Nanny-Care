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
    # selected_nanny = Nanny.objects.get(id=request.nanny_id)
    selected_nanny = Nanny.objects.all()[0]
    params = {'nanny': selected_nanny}
    
    return render(request, 'book/booking.html', params)


def welcome(request):
    nanny = Nanny.objects.all()
    return render(request, 'nannydetails/nannydetails.html', {'nanny':nanny})


def companydetails(request):
    
    return render (request, 'companydetails/company_detail.html')
