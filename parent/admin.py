from django.contrib import admin

from .models import TrainingConversation

# Register your models here.
@admin.register(TrainingConversation)
class ConvoAdminModel(admin.ModelAdmin):

   
    model = TrainingConversation
    list_display = ['id', 'data', 'datetime']