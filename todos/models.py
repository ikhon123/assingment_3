from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255)
    todo = models.TextField()
    date = models.DateField()
    
    def __unicode__(self):
        return self.title