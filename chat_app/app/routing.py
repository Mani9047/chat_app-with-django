from django.urls import path

from .consumers import ChatConsumer
websocket_patterns=[
    path('ws/<group_name>/',ChatConsumer.as_asgi())
]