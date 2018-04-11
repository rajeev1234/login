from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Contact_Us(models.Model):
    Contact_Us_User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Contact_Us')

    Contact_Us_Subject = models.CharField(max_length=100)
    Contact_Us_Message = models.TextField(max_length=1000)

    def __str__(self):
        return self.Contact_Us_Subject

    def get_absolute_url(self):
        return reverse('contact_us_details', args=[str(self.id)])