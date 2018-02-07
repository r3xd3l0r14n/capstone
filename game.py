import json
from player import Player
from deck import Deck

class Game:

    def __init__(self):
        self._last_id = 0
        self._players = {}

    def new_player(self, name):
        self._last_id += 1
        player_id = self._last_id
        # self.send_personal(ws, "handshake", name, player_id)

        player = Player(player_id, name)
        self._players[player_id] = player
        return player

    def join(self, id):
        return self._players[id]

    def get_players_names(self, id):
        s = {}
        for k, p in self._players.items():
            s[k] = p.name
        return s

    def disconnect_player(self, id):
        delUserName = self._players[id].name
        del self._players[id]
        return delUserName