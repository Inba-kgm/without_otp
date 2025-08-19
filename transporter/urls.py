from django.urls import path,include
from.views import *

urlpatterns = [
    path('index/',index,name='index'),
    path('history/',history,name='history'),
    path('transhistory/',history,name='transhistory'),
    path('transdelivered/',transdelivered,name='transdelivered'),
    path('profile/',profile,name='profile'),
    path('search/',search,name='search'),
    path('accepted/',accepted,name='accepted'),
    path('delacc/',delacc,name='delacc'),
]