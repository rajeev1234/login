from django.db import models

class Past_Work(models.Model):
    Title = models.CharField(max_length=100)
    #Client = models.ForeignKey()
    Company_Role = models.CharField(max_length=100)
    Work_Status = models.CharField(max_length=100)
    Image = models.ImageField()
    Video = models.FileField()
    From_Duration = models.DateField()
    To_Duration = models.DateField()


    def __str__(self):
        return self.Title