from django.shortcuts import render
import json
import datetime
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
import uuid
from bson.json_util import dumps, loads 
from django.urls import reverse
from django.core.serializers import serialize
# Create your views here

class SendTemplateMailView(APIView):

    def post(self, request, *args, **kwargs):
            for i in request.data['recipient_list']:
                try:
                    user=emailData.objects.get(email = i)
                except emailData.DoesNotExist:
                    user = emailData.objects.create(email = i)                
                user.unique_code = uuid.uuid4()
                user.save()
                template = get_template("mail.html")
                context_data = dict()
                context_data["image_url"] = request.build_absolute_uri(("image_load"))
                print(context_data['image_url'])
                context_data['user']="Vishal"
                url_is = context_data["image_url"]+"/"+str(user.unique_code)+"/"
                context_data['url_is']= url_is
                html_text = template.render(context_data)
                email = user.email
                subject, from_email, to = request.data['subject'], 'tt0367816@gmail.com',  [i]

                msg = EmailMultiAlternatives(subject, html_text, from_email, to)
                msg.attach_alternative(html_text, "text/html")
                msg.content_subtype='html'
                msg.send()
                print("done", email)
            
            return Response({"success":True})

# api tp retrieve data

class getdata(APIView):

    def get(self,request):
        data = serialize('json', emailData.objects.all())
        return Response({"data":data})


    



@api_view()
def image_load(request, uuid_val):
   
    if request.method =='GET':
        print("\nImage Loaded\n")
        red = Image.new('RGB', (20, 20))
        response = HttpResponse(content_type="image/png" , status = status.HTTP_200_OK)
        user = emailData.objects.get(unique_code= uuid_val)
        if user.status==0:
            user.open_date=datetime.datetime.today()
        user.status=user.status+1
        user.save()
        red.save(response, "PNG")
        print("hit")
        return response