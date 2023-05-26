from django.db import models

# Create your models here.

class emailData(models.Model):
    receiver=models.CharField(max_length=100,null=True)
    subject=models.CharField(max_length=100)
    read=models.CharField(max_length=10,null=True)
    def __str__(self):
        return self.receiver