# Email-Tracking

## About 

This following API is used to track whether email has been opened by user or not. This can help various businesses to find out analytics of there email campaign

This is an open to contibute project feel free to connect


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

