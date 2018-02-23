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
        self._last_id += 1
        player_id = self._last_id
        # self.send_personal(ws, "handshake", name, player_id)

        player = Player(player_id, name)
        self._players[player_id] = player
        return player

    def join(self, id):
        return self._players[id]

    def get_players_names(self):
        s = {}
        for k, p in self._players.items():
            s[k] = p.name
        return s

    def disconnect_player(self, id):
        delUserName = self._players[id].name
        del self._players[id]
        return delUserName

    def init_game(self):  # first_ply):
        i = 1
        if self.checkEnoughPlayers():
            self.deck.shuffle()
            rtnMsg = {'Deck': self.deck.getDeck(), 'Hands': {}}
            hands = self.deck.dealHands(len(self._players))
            while i <= len(self._players):
                self._players[i].hand = hands[i]
                rtnMsg['Hands'][i] = (self._players[i].hand.getHandDict())
                i += 1
                print(rtnMsg)
        else:
            rtnMsg = {'msg': 'Failure to start game, not enough players'}
        return rtnMsg

    def checkEnoughPlayers(self):
        if len(self._players) >= 1:
            msg = True
        else:
            msg = False
        return msg

#    def turn_update(self, turn):
#        rtnMsg = {'Turn': self._players[turn]._id}
#        return rtnMsg

    def updateGame(self, card):
        print('The card that was fished for was %s' % card)
        return card
'''
    def checkQuit(self, player):
        function to ensure player did not
        disconnect from game 
        
    def checkEnd(self):
        function to check for empty deck and/or
        empty hands
        
    def gameUpdate(self, turn, cardFishedfor, matches, etc)
        function that returns a dict of information to 
        message handler
'''
    def game_loop(self):
        turn = 1
        scores = {}
        last_person = len(self._players)

''' The logic behind this if/else is to reduce the number of functions 
    communicating with the front end, instead of init_game, we just use
    the game loop. This way the loop won't even begin if the requirements
    aren't met, the 'not enough players' message is still sent.
'''
        if self.checkEnoughPlayers():
            self.init_game()
            while True:
        #        create a checkEnd()
        #        checkQuit() # create a checkQuit()
                if turn < last_person:
                    currentPlayer = self._players[turn]
    #                checkQuit()

                    if updateGame(card):
                        if self.player.checkHand(rank):
                            cardAdded = currentPlayer.addCard(card)
                            cardRemoved = self._players[opponent].removeMatch(card)
                            if self.player.fourKind():
                                    scores[turn] += 1

                    else:
#                        checkQuit()
                        turn += 1
                        if self.deck.numCards() > 0:
                            player.draw()
                        self.player.fourKind()
                        if self.player.fourKind():
                            scores[turn] += 1
#                        if checkIfWon():
#                           break

                else:
                    currentPlayer = self._players[turn]
#                    checkQuit()

                    if updateGame(card):
                        if self.player.checkHand(rank):
                            cardAdded = currentPlayer.addCard(card)
                            cardRemoved = self._players[opponent].removeMatch(card)
                            if self.player.fourKind():
                                    scores[turn] += 1
                        else:
#                            checkQuit()
                            turn = 1
                            if self.deck.numCards() > 0:
                                player.draw()
                            self.player.fourKind()
                            if self.player.fourKind():
                                scores[turn] += 1
#                            if checkIfWon():
#                                break  
        else:
            self.init_game()
'''