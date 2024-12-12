# your_app_name/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class MyAsyncConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['editor_id']
        print(self.user_id)
        self.group_name = f"Editor_{self.user_id}"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message', '')

        
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat_message',
                'message': message,
            }
        )

    async def chat_message(self, event):
        message = event['status']

        # Send the message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
        }))
