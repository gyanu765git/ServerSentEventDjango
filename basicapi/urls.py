from django.urls import path
from .views import CollectDataStream,collectData,CollectDataStreamAPI

urlpatterns = [
    path('collect-data-stream/', CollectDataStream, name='collect_data_stream'),
    path('collect-data/', collectData, name='collect_data_view'),
    path('collect/', CollectDataStreamAPI.as_view(), name = "show_record")
]
