from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=500,blank=False,null=False)
    description = models.TextField(blank=False,null=False)
    date_created = models.DateField(auto_now_add=True)
    date_completed = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.title