from django.db import models

# Create your models here.

class Group(models.Model):
    group=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.group
    
class Message(models.Model):
    group=models.ForeignKey('Group',on_delete=models.CASCADE)
    message=models.CharField(max_length=200)
    timestemp=models.DateTimeField(auto_now_add=True)