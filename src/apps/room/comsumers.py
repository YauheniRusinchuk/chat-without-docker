from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer


class CommentCunsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept",
        })
        print("SOCKET MSG ...")

    async def websocket_receive(self, event):
        print('receive ...', event)

    async def websocket_disconnect(self, event):
        print("disconnect")
