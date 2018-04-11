from django.db import models

# Create your models here.


class news(models.Model):
    name=models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    friend =models.ForeignKey("self",related_name='referral',on_delete=models.CASCADE,null=True,blank=True)
    ip_address = models.CharField(max_length=120,default='apple')
    ref_id = models.CharField(max_length=120)

    time =models.DateTimeField(auto_now_add= True,auto_now=False)
    update = models.DateField(auto_now_add=False,auto_now=True)


    def __str__(self):
        return "%s" %(self.email)
