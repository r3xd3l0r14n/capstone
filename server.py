import os
import asyncio
import json
from aiohttp import web

#import settings
from game import Game


async def handle(request):
    ALLOWED_FILES = ["index.html", "style.css"]
    name = request.match_info.get('name', 'index.html')
    if name in ALLOWED_FILES:
        try:
            with open(name,'rb') as index:
                return web.Response(body=index.read(), content_type='text/html')
        except FileNotFoundError:
            pass
    return web.Response(status=404)


async def wshandler(request):
    print("Connected")
    app = request.app
    ws = web.WebSocketResponse()

    player = None
    while True:
        msg = await ws.receive()
        if msg.tp == web.MsgType.text:
            print("Got message %s"%msg.data)

            data = json.loads(msg.data)
            if not player:
                if data[0] == "new_player":
                    player = game.new_player(data[1], ws)