from django.urls.conf import path
from . import views
urlpatterns = [
    path('/home', views.home, name='home'),
]
