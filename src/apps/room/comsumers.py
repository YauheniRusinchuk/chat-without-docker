from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from src.models.room.models import Room
from src.models.message.models import Message
import json


class CommentCunsumer(AsyncConsumer):


    async def websocket_connect(self, event):
        pk_room         = self.scope['url_route']['kwargs']['pk']
        room            = Room.objects.get(pk=pk_room)
        self.room       = room
        self.pk_room    = "id" + str(pk_room)
        await self.channel_layer.group_add(
            self.pk_room,
            self.channel_name,
        )
        await self.send({
            "type": "websocket.accept",
        })


    async def websocket_receive(self, event):
        text_comment = event.get('text', None)
        if text_comment is not None:
            load_data   = json.loads(text_comment)
            message     = load_data.get('message')
            user        = self.scope['user']
            response = {
                'message': message,
                'username': user.username,
            }
            await self.create_comment(user, message)
            await self.channel_layer.group_send(
                    self.pk_room,
                {
                    "type": "msg_comment",
                    "text": json.dumps(response),
                }
            )


    async def msg_comment(self, event):
        await self.send({
            "type": "websocket.send",
            "text": event["text"]
        })


    @database_sync_to_async
    def create_comment(self, user, msg):
        Message.objects.create(author=user, text=msg, room=self.room)



    async def websocket_disconnect(self, event):
        await self.channel_layer.group_discard(
            self.pk_room,
            self.channel_name
        )
