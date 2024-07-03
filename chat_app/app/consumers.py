from channels.generic.websocket import SyncConsumer
from channels.layers import get_channel_layer
from .models import Group, Message
from asgiref.sync import async_to_sync
import json
class ChatConsumer(SyncConsumer):
    def websocket_connect(self, event):
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.send({
            "type": "websocket.accept",
            })
        
        
    
    def websocket_receive(self, event):
        data = json.loads(event['text'])
       
        group = Group.objects.get(group=self.group_name)
        obj = Message(
                group=group,
                message=data['message']
            )
        obj.save()
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
                {
                    'type': 'chat.message',
                    'message':json.dumps(data)
                }
            )
    
    def chat_message(self, event):
        self.send({
            'type': 'websocket.send',
            'text':event['message']
        })
    
    def websocket_disconnect(self, event):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )
        self.close()
