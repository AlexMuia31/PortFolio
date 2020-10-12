from django.db import models

class Job(models.Model):
    Title=models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    summary =models.CharField(max_length=200)

    def __str__(self):
        return self.Title
    


