from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title= models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body= RichTextField(blank= True, null= True)
    #body = models.TextField()
    image = models.ImageField(upload_to='images/')



    def __str__(self):
        return self.title
    

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')