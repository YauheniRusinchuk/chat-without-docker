from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from src.models.room.models import Room
import json


class CommentCunsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        pk_room         = self.scope['url_route']['kwargs']['pk']
        room            = Room.objects.get(pk=pk_room)
        self.post       = room
        self.pk_room    = "id" + str(pk_room)
        await self.channel_layer.group_add(
            self.pk_room,
            self.channel_name,
        )
        await self.send({
            "type": "websocket.accept",
        })
        print("SOCKET MSG ...")

    async def websocket_receive(self, event):
        print('receive ...', event)
        text_comment = event.get('text', None)
        if text_comment is not None:
            load_data   = json.loads(text_comment)
            message     = load_data.get('message')
            user        = self.scope['user']


    async def websocket_disconnect(self, event):
        print("disconnect")
