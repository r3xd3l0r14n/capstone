import json
from player import Player


class Game:

    def __init__(self):
        self._last_id = 0
        self._players = {}

    def new_player(self, name, ws):
        self._last_id += 1
        player_id = self._last_id
        self.send_personal(ws, "handshake", name, player_id)

        player = Player(player_id, name, ws)
        self._players[player_id] = player
        return player

    def join(self, player):
        self.send_all("p_joined", player._id, player.name)

    def send_personal(self, ws, *args):
        msg = json.dumps([args])
        ws.send_str(msg)

    def send_all(self, *args):
        self.send_all_multi([args])

    def send_all_multi(self, commands):
        msg = json.dumps(commands)
        for player in self._players.values():
            if player.ws:
                player.ws.send_str(msg)