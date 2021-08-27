from django.db import models

# Create your models here.
class SharkInfo(models.Model):
    title = models.CharField(max_length=150)
    strength = models.CharField(max_length=150)
    speed = models.CharField(max_length=150)
    iq = models.CharField(max_length=150)
    image = models.ImageField(upload_to = 'images/',blank=True,null=True)

    def __str__(self):
        return self.title