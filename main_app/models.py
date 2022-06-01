from django.db import models

# Create your models here.
class Car(models.Model):

    name = models.CharField(max_length=100)
    year = models.TextField(max_length=4)
    bio = models.TextField(max_length=500, default='Car Bio')
    img = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']