from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('sendEmail',views.EmailAPI.as_view(),name='send_template'),
    path('render_image/',views.render_image, name='render_image'),
]
