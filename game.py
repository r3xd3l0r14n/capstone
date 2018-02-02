import json
from player import Player


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
        for p in self._players:
            if id == p._id:
                print("id already exists in table")
            s = ''.join(("\"", p.name, "\","))
        return "[" + s[:-1] + "]"
