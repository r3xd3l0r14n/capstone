import json
from player import Player
from deck import Deck
import random
from flask_socketio import emit


class Game:

    def __init__(self):
        self._last_id = 0
        self._players = {}
        self.deck = Deck()
        # self.player = Player()

    def new_player(self, name):
        player_id = self._last_id
        # self.send_personal(ws, "handshake", name, player_id)

        player = Player(player_id, name)
        self._players[player_id] = player
        self._last_id += 1
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

    def init_game(self):  # first_ply):
        i = 0
        if self.checkEnoughPlayers():
            self.deck.shuffle()
            rtnMsg = {'game': '1', 'Deck': self.deck.getDeck(), 'Hands': {}}
            hands = self.deck.dealHands(len(self._players) - 1)
            while i <= len(self._players) - 1:
                self._players[i].hand = hands[i]
                rtnMsg['Hands'][i] = (self._players[i].hand.getHandDict())
                i += 1
        else:
            rtnMsg = {'game': '0', 'msg': 'Failure to start game, not enough players'}
        return rtnMsg

    def checkEnoughPlayers(self):
        if len(self._players) >= 2:
            msg = True
        else:
            msg = False
        return msg

    def whoFirst(self):
        who_list = [x for x in self._players]
        num_of_players = len(self._players)
        return who_list[random.randrange(0, num_of_players)]

    def turn_update(self, turn):
        rtnMsg = {'Turn': self._players[turn]._id}
        return rtnMsg

    '''
    def checkQuit(self, player):
        function to ensure player did not
        disconnect from game 
        
    def checkEnd(self):
        function to check for empty deck and/or
        empty hands
        
    def gameUpdate(self, turn, cardFishedfor, matches, etc)
        function that returns a dict of information to 
        message handler '''

    # def game_loop(self):
    #     self.init_game()
    #     turn = self.whoFirst()
    #     last_person = len(self._players)
    #     scores = {}
    #     # create a checkEnd()
    #     checkQuit() # create a checkQuit()
    #     while True:
    #         if turn < last_person:
    #             currentPlayer = self._players[turn]
    #             turn_update(turn)
    #             checkQuit()
    '''
    Need to discuss with Colin about what information will
    be returned from clicks

    if event.type == mouseClick:
        if position IVO of x:
            opponent = 1
        elif position IVO of y:
            opponent = 2
        else:
            if card.clicked(position):
                call a func to return selected card value
                if self.player.checkHand(rank):
                    cardAdded = currentPlayer.addCard(card)
                    cardRemoved = self._players[opponent].removeMatch(card)
                    if self.player.fourKind():
                            scores[turn] += 1
                else:
                    checkQuit()
                    turn += 1
                    if self.deck.numCards() > 0:
                        player.draw()
                    self.player.fourKind()
                    if self.player.fourKind():
                        scores[turn] += 1
                    checkIfWon()

else:
    currentPlayer = self._players[turn]
    turn_update(turn)
    checkQuit()

    Need to discuss with Colin about what information will
    be returned from clicks

    if event.type == mouseClick:
        if position IVO of x:
            opponent = 1
        elif position IVO of y:
            opponent = 2
        else:
            if card.clicked(position):
                call a func to return selected card value
                if self.player.checkHand(rank):
                    cardAdded = currentPlayer.addCard(card)
                    cardRemoved = self._players[opponent].removeMatch(card)
                    if self.player.fourKind():
                            scores[turn] += 1
                else:
                    checkQuit()
                    turn = 1
                    if self.deck.numCards() > 0:
                        player.draw()
                    self.player.fourKind()
                    if self.player.fourKind():
                        scores[turn] += 1
                    checkIfWon()
                    '''
