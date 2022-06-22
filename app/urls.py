from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('profile/<str:username>/', views.profile, name='profile'),
    path('booking/', views.booking, name='booking'),
    path('', views.welcome, name='welcome'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
