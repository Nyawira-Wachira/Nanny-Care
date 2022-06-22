from django.contrib import admin
from .models import Nanny, Bio, UserProfile

# Register your models here.
admin.site.register(Nanny)
admin.site.register(Bio)
admin.site.register(UserProfile)