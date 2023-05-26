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
# Create your views here.

class sendEmail(APIView):
    def send_email(self,recipient_email, subject, message):
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587

        email = MIMEMultipart()
        email['From'] = 'tt0367816@gmail.com'
        email['To'] = recipient_email
        email['Subject'] = subject

        email.attach(MIMEText(message+f" http://127.0.0.1:8000/getTrack/{recipient_email}/{subject}", 'plain'))

        with smtplib.SMTP(smtp_server,smtp_port) as server:
            server.starttls() 
            server.login(config('id'), config('apppass'))
            server.send_message(email)

    def post(self, request):
        try:
            serializer = emailSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.send_email(request.data['email'],request.data['subject'],request.data['body'])
            return Response(serializer.data)
        except:
            return Response({'result':"wrong data passed"})
        



class getTrack(APIView):
     def get(self,request,**kwargs):
        try:
            receivera = str(kwargs.get('email', None))
            subjecta = str(kwargs.get('subject', None))
            print(receivera,subjecta)
            data = emailData(receiver=receivera,subject=subjecta,read='True')
            data.save()
            return Response("done")
        except:
            return Response({'result':"wrong data passed"})

            
          