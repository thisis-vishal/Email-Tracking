from django.db import models

# Create your models here.

class emailData(models.Model):
    email = models.EmailField(max_length = 254 , blank= True , null=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.email