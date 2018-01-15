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
    game = app["game"]
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    player = None
    while True:
        msg = await ws.receive()
        if msg.tp == web.MsgType.text:
            print("Got message %s" % msg.data)

            data = json.loads(msg.data)
            if not player:
                if data[0] == "new_player":
                    player = game.new_player(data[1], ws)
            elif data[0] == "join":
                game.join(player)
        elif msg.tp == web.MsgType.close:
            break

    print("Closed Connection")
    return ws

# TODO fill with basic game Loop code (should be calling the game functions to handle dealing and decks)
# async def game_loop(game):

event_loop = asyncio.get_event_loop()
event_loop.set_debug(True)

app = web.Application()

app["game"] = Game()

app.router.add_route('GET', '/connect', wshandler)
app.router.add_route('GET', '/{name}', handle)
app.router.add_route('GET', '/', handle)

port = int(os.environ.get('PORT', 8080))
web.run_app(app, port=port)


