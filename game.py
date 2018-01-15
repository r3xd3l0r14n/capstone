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