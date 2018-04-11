from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Enquiry(models.Model):
    Enquiry_Subject_choices = (
        ('FEATURE FILM PRODUCTION', 'FEATURE FILM PRODUCTION'),
        ('TVC/CORPORATES/AV’s', 'TVC/CORPORATES/AV’s'),
        ('FILMING/EVENT PERMISSIONS', 'FILMING/EVENT PERMISSIONS'),
        ('AUGMENTED REALITY CAMPAIGNS', 'AUGMENTED REALITY CAMPAIGNS'),
        ('3D DESIGNING/MODELING/WALKTHROUGHS/ANIMATIONS', '3D DESIGNING/MODELING/WALKTHROUGHS/ANIMATIONS'),
        ('IT CONSULTANCY', 'IT CONSULTANCY'),
        ('APPLICATION DEVELOPMENT/WEB DESIGNING', 'APPLICATION DEVELOPMENT/WEB DESIGNING'),
        ('MOBILE APPLICATION DEVELOPMENT', 'MOBILE APPLICATION DEVELOPMENT'),
        ('WEBCASTING SERVICES end to end', 'WEBCASTING SERVICES end to end'),
        ('CORPORATE IDENTITIES/BRAND BUILDING', 'CORPORATE IDENTITIES/BRAND BUILDING'),
        ('CREATIVE CONSULTANCY', 'CREATIVE CONSULTANCY'),
        ('PRINT DESIGNING', 'PRINT DESIGNING'),
        ('EVENTS', 'EVENTS'),




    )
    Enquiry_User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Enquiry')

    Enquiry_Subject = models.CharField(max_length=100,choices=Enquiry_Subject_choices)
    Enquiry_Message = models.TextField(max_length=1000)

    def __str__(self):
        return self.Enquiry_Subject

    def get_absolute_url(self):
        return reverse('enquiry_details', args=[str(self.id)])