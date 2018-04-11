from django.db import models

class Work(models.Model):
    Title = models.CharField(max_length=100)
    # Client = models.ForeignKey()
    Company_Role = models.CharField(max_length=100)
    Work_Status = models.CharField(max_length=100)
    Image = models.ImageField()
    Video = models.FileField()
    Completed = models.BooleanField()
    On_Going = models.BooleanField()




    def __str__(self):
        return self.Title

