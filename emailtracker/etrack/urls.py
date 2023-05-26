from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('sendEmail',views.sendEmail.as_view()),
    path('getTrack/<email>/<subject>',views.getTrack.as_view())
]
