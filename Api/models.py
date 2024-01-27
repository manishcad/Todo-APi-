from django.db import models

# Create your models here.

class Todo_Model(models.Model):
    task=models.CharField(max_length=225)
    is_complete=models.BooleanField(default=False)

    def __str__(self):
        return self.task