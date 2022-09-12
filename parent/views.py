from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser

from chatterbot import ChatBot  
from chatterbot.trainers import ListTrainer  
from chatterbot.trainers import ChatterBotCorpusTrainer


from .models import TrainingConversation


vp_bot = ChatBot(  
    name = 'Sara',  # semi-automated-robotic-AI
    read_only = True,  
    logic_adapters = [  
        # 'chatterbot.logic.MathematicalEvaluation',  
        'chatterbot.logic.BestMatch'  
        ],
              
)  

trainer = ChatterBotCorpusTrainer(vp_bot)

trainer.train('chatterbot.corpus.english')

# Now we can export the data to a file
trainer.export_for_training('./my_export.json')

list_trainee = ListTrainer(vp_bot)  


@api_view(['POST'])
def talk_view(request):
    print("Requets: ", vp_bot.get_response("hello"))
    return Response({"message": str(vp_bot.get_response(request.data.get('text')))})


@api_view(['GET'])
# @permission_classes([IsAdminUser])
def train_data_view(request):

    list_trainee.train([x.data for x in TrainingConversation.objects.all()])  
    
    return Response(status=status.HTTP_200_OK)