class Player:

    def __init__(self, player_id, name, ws):
        self._id = player_id
        self.name = name
        self.ws = ws

    def toString(self):
        return self.name, self._id