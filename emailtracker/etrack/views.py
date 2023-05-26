from django.shortcuts import render
import json
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from . serializer import *
from rest_framework.response import Response
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from decouple import config
from .models import emailData
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from rest_framework import status
from PIL import Image
from django.template import Context
from django.template.loader import get_template
# Create your views here



class EmailAPI(APIView):
    def get(self, request,*args, **kwargs):
        target_user_email = request.data['recipient_list']
        mail_template = get_template("mail.html")
        context_data_is = dict()
        context_data_is["image_url"] =   request.build_absolute_uri(("render_image"))
        url_is = context_data_is["image_url"]
        context_data_is['url_is']= url_is
        html_detail = mail_template.render(context_data_is)
        subject, from_email,to = request.data['subject'],  config('id'), [target_user_email]
        
    
        msg = EmailMultiAlternatives(subject, html_detail, from_email, to)
        msg.content_subtype='html'
        msg.send()
        return Response({"success":True})

            
@api_view()
def render_image(request):
     if request.method =='PUT':
        image= Image.new('RGB', (20, 20))
        response = HttpResponse(content_type="image/png" , status = status.HTTP_200_OK)
        user = emailData.objects.get(id = 1)
        user.status = True
        user.save()
        image.save(response, "PNG")
        return response