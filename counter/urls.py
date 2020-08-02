from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='counter-home'),
    path('nos',views.nos,name='counter-result')
]