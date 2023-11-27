from djongo import models
import random
# Create your models here.

class emailData(models.Model):
    email = models.EmailField(max_length = 254 , blank= True , null=True)
    status = models.IntegerField(default=0)
    unique_code = models.UUIDField(null=True, blank=True , unique=True)
    open_date=models.DateTimeField(null=True)
    def __str__(self):
        return self.email