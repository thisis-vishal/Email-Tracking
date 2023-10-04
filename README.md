# Email-Tracking

## Description

This following API is used to track whether email has been opened by user or not. This can help various businesses to find out analytics of there email campaign

This is an open to contribute project feel free to connect

I am using Pixels technology to make this project 

[Follow this url to learn about pixels ](https://www.nutshell.com/blog/email-tracking-pixels-101-how-do-tracking-pixels-work)


***


## Pre Requisite 

* asgiref==3.7.1
* Django==4.1.9
* django-cors-headers==4.0.0
* djangorestframework==3.14.0
* djongo==1.3.6
* dnspython==2.3.0
* Pillow==9.5.0
* pymongo==3.12.1
* python-decouple==3.8
* pytz==2023.3
* sqlparse==0.2.4
* typing_extensions==4.6.2
* tzdata==2023.3
* python==3.9

***

## How to Use

API endpoint: _https://email-tracking-five.vercel.app/_

### Use send API call to send email to users:

use _/send_ API to send emails, Prameters fro send API are: 

**"recipient_list"** : one should enter the list of email strings 

**"subject"** : one should enter the subject of email


![postmanimg](https://github.com/thisis-vishal/Email-Tracking/blob/main/emailtracker/screenshots/Screenshot%202023-03-05%20153045.png)


### The result will be stored in mongodb database like below image:


![compassimg](https://github.com/thisis-vishal/Email-Tracking/blob/main/emailtracker/screenshots/Screenshot%202023-10-04%20143453.png)


***

## To contribute 

**Change DATABASE parameters in settings.py**

`DATABASES = {

        'default': {

        'ENGINE': 'djongo',

        "CLIENT": {

        "host": f"mongodb+srv://{os.getenv('mongouserid')}:{os.getenv('mongopass')}@cluster0.b1vrwir.mongodb.net/?retryWrites=true&w=majority",

        "username": os.getenv('mongouserid'),

        "password": os.getenv('mongopass'),

        "name": "emailtrack",

        "authMechanism": "SCRAM-SHA-1",

        },
    }
}`


Enter your cluster details by creating one on mongoDB Atlas

**Then add your email id details you are using for sending emails**


`EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.getenv('id')
EMAIL_HOST_PASSWORD =os.getenv('apppass')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_TIMEOUT = 300 # in seconds
DEFAULT_FROM_EMAIL = 'tt0367816@gmail.com'`

First make an email which allow to send email through 3rd party application

[Follow this to make TEST email](https://support.google.com/accounts/thread/12835078/how-to-allow-access-for-less-secure-app-to-interact-with-gmail-account-use-smtp-server-to-send-mail?hl=en)

***

After successfully following above steps you can create API to send and track email

_**Important Note**_ : You can only use these kind of APIs once after deploying it on any deployment servers



