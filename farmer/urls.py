from django.urls import path,include
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('entry',home,name='home'),
    path('farmhome/',farmhome,name='farmhome'),
    path('farmprofile/',farmprofile,name='farmprofile'),
    path('farmupload/',farmupload,name='farmupload'),
    path('farmorders/',farmorders,name='farmorders'),
    path('publish/',publish,name='publish'),
    path('acceptcarts/',acceptcarts,name='acceptcarts'),
    path('removes/',removes,name='removes'),
    path('removeorder/',removeorder,name='removeorder'),
    path('farmpending/',pending,name='farmpending'),
    path('farmshipped/',shipped,name='farmshipped'),
    path('farmdelivered/',delivered,name='farmdelivered'),
    path('farmcancelled/',cancelled,name='farmcancelled'),
    path('editprofile/',editprofile,name='editprofile'),
    path('farmallorders/',allorders,name='farmallorders'),
    path('changeinfo/',changeinfo,name='changeinfo'),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
