import json
from player import Player


class Game:

    def __init__(self):
        self._last_id = 0
        self.players = {}

    def new_player(self, name):
        self._last_id += 1
        player_id = self._last_id
        player = Player(player_id, name)
        self.players[player_id] = player

        return self.send_personal("handshake", name, player_id)

    def join(self, player):
        return self.send_personal("p_joined", player._id, player.name)

    def send_personal(self, *args):
        msg = json.dumps([args])
        return msg

