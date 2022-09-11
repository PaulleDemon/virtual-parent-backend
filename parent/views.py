from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser


from chatterbot import ChatBot  
from chatterbot.trainers import ListTrainer  


from .models import TrainingConversation


vp_bot = ChatBot(  
    name = 'Sara',  # semi-automated-robotic-AI
    read_only = True,  
    logic_adapters = [  
        'chatterbot.logic.MathematicalEvaluation',  
        'chatterbot.logic.BestMatch'  
        ]  
)  

list_trainee = ListTrainer(vp_bot)  


@api_view(['GET'])
def talk_view(request, talk):
    return Response({"message": vp_bot.generate_response(talk)})


@api_view(['GET'])
@permission_classes(IsAdminUser)
def train_data_view(request):

    list_trainee.train(TrainingConversation.objects.all())  
    
    return Response(status=status.HTTP_200_OK)