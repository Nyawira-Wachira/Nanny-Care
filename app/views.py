from django.shortcuts import render, redirect, get_object_or_404


from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

from .models import User, Nanny, Bio, UserProfile
from .forms import UpdateProfileForm,UpdateUserForm

# Create your views here.
def Index(request):
    return render(request, 'index.html')


@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='/accounts/login/')
def profile(request, username):
    user = get_object_or_404(User, username=username)
    
    if request.method == 'POST':
        user_form=UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect('profile', username=request.user.username)
        
    else:
        profile_form = UpdateProfileForm()
        user_form =UpdateUserForm(instance=request.user)
    
    context = {
        'user': user,
        'form': profile_form,
        'user_form': user_form,
    }
    return render(request, 'profile/profile.html', context)



@login_required(login_url='/accounts/login/')
def booking(request):
    # selected_nanny = Nanny.objects.get(id=request.nanny_id)
    selected_nanny = Nanny.objects.all()[0]
    params = {'nanny': selected_nanny}
    
    return render(request, 'book/booking.html', params)


def details(request):
    
    nanny = Nanny.objects.all()
    return render(request, 'nannydetails/nannydetails.html', {'nanny':nanny})


@login_required(login_url='/accounts/login/')
def companydetails(request):
    gallery = Nanny.objects.all() [:8]

    return render (request, 'companydetails/company_detail.html',{'gallery':gallery})
