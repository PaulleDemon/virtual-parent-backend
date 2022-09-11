from django.db import models

# Create your models here.

class TrainingConversation(models.Model):

    data = models.TextField(max_length=400)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = 'training conversation'
        verbose_name_plural = 'training conversation'


