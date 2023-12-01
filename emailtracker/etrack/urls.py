from django.urls import path , include
from .views import SendTemplateMailView , image_load , getdata
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    
    path('image_load/<str:uuid_val>/',image_load, name='image_load'),
    
    path('send', SendTemplateMailView.as_view(), name= 'send_template'),
    path('get',getdata.as_view(),name="all data")
]
