from django.dispatch import receiver
from django.db.models.signals import post_save

from . import models


# @receiver(post_save, sender=models.TrainingConversation)
# def check_threshold_crossed(sender, instance, created, *args, **kwargs):

#     """
#         checks if the threshold has been passed to mark it as created.
#     """

#     if created:
#         pass

