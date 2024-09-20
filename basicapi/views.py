from rest_framework.views import APIView
from .models import CollectData
from .serializers import CollectDataSerializer

import time
from django.http import StreamingHttpResponse
import json

from django.shortcuts import render
from django.views.decorators.http import require_GET

import logging
logger = logging.getLogger(__name__)

def event_stream():
    while True:
        try:
            latest_data = CollectData.objects.all()
            serializer_data = CollectDataSerializer(latest_data, many=True).data
            logger.info(f"Yielding data: {serializer_data}") 
            yield f"data: {json.dumps(serializer_data)}\n\n"
        except Exception as e:
            logger.error(f"Error occurred: {e}")
        time.sleep(1)


############### MVT Architecture ###########################
@require_GET
def CollectDataStream(request):
    response = StreamingHttpResponse(event_stream(), content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache' 
    return response

def collectData(request):
    return render(request, 'index.html')

#################################################################


##################### MVC Architecture(Rest API) ################
class CollectDataStreamAPI(APIView):
    @staticmethod
    def get(request):
        response = StreamingHttpResponse(event_stream(), content_type='text/event-stream')
        response['Cache-Control'] = 'no-cache' 
        return response

#################################################################