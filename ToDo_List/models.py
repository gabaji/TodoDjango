from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TodoEntry(models.Model):
    work = models.CharField(max_length=100)
    parentuser = models.ForeignKey(User,on_delete = models.CASCADE)
    time = models.DateField(blank=False,null=False,auto_now=True)

    class Meta:
        verbose_name_plural = 'Todo Entries'
