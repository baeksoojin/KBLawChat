from django.db import models

# Create your models here.

class Message(models.Model):
    checked = models.IntegerField()
    question = models.CharField(max_length=300, blank=True, null=True)
    answer = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'message'