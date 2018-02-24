import json

from card import Card
from player import Player
from deck import Deck
import random
from flask_socketio import emit


class Game:

    def __init__(self):
        self._last_id = 0
        self._players = {}
        self.deck = Deck()
        #self.player = Player()

    def new_player(self, name):
        self._last_id += 1
        player_id = self._last_id

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
            hands = self.deck.dealHands(len(self._players))
            rtnMsg = {'Deck': self.deck.getDeck(), 'Hands': {}}
            while i <= len(self._players):
                self._players[i].hand = hands[i]
                rtnMsg['Hands'][i] = (self._players[i].hand.getHandDict())
                i += 1
                #print(rtnMsg)
        else:
            rtnMsg = {'msg': 'Failure to start game, not enough players'}
        return rtnMsg

    def checkEnoughPlayers(self):
        if len(self._players) >= 1:
            msg = True
        else:
            msg = False
        return msg

    def stripMsg(self, msg):
       # print(msg['card'])
        nMsg = msg['card'].split(' ')
        return nMsg

    #    def turn_update(self, turn):
    #        rtnMsg = {'Turn': self._players[turn]._id}
    #        return rtnMsg

    def updateGame(self, card):
        #print('The card that was fished for was %s' % card)
        return True

    def newUpdateGame(self):  # first_ply):
        i = 1
        rtnMsg = {'Hands': {}}
        while i <= len(self._players):
             rtnMsg['Hands'][i] = (self._players[i].hand.getHandDict())
             i += 1
        return rtnMsg

    def suitCheck(self, s):
        rtn = 0
        if s == 'c':
            rtn = 0
        elif s == 'd':
            rtn = 1
        elif s == 'h':
            rtn = 2
        elif s == 's':
            rtn = 3
        else:
            print("Fuck it")
        return rtn

    def game_loop(self, msg):
        turn = msg['id']
        scores = {}
        last_person = len(self._players)
        strip = self.stripMsg(msg)
        suit = self.suitCheck(strip[1])
        card = Card(suit, int(strip[0]))

        # if self.checkEnoughPlayers():
        # self.init_game()
        # while True:
        # if turn < last_person:
        currentPlayer = self._players[turn]
        if (currentPlayer._id +1) <= 4:
            opponent = self._players[turn+1]
        else: opponent = self._players[1]
        if self.updateGame(card):
            print('made it here')
            if opponent.checkHand(card):
                cardAdded = currentPlayer.hand.addCard(card)
                cardRemoved = opponent.removeMatch(card)  # changed opponent to player+1
                if currentPlayer.fourKind():
                    scores[turn] += 1
        else:
            #                        checkQuit()
            turn += 1
            print(turn)
            if self.deck.numCards() > 0:
                currentPlayer.draw()
            if currentPlayer.fourKind():
                scores[turn] += 1
        return self.newUpdateGame()

    #                        if checkIfWon():
    #                           break

    # else:
    #     currentPlayer = self._players[turn]
    #     #                    checkQuit()
    #
    #     if self.updateGame(card):
    #         if self.player.checkHand(rank):
    #             cardAdded = currentPlayer.addCard(card)
    #             cardRemoved = self._players[opponent].removeMatch(card)
    #         if self.player.fourKind():
    #             scores[turn] += 1
    #     else:
    #         #                            checkQuit()
    #         turn = 1
    #         if self.deck.numCards() > 0:
    #             player.draw()
    #         self.player.fourKind()
    #         if self.player.fourKind():
    #         #             scores[turn] += 1
    # else:
    #     self.init_game()


#                            if checkIfWon():
#                                break

#        create a checkEnd()
#        checkQuit() # create a checkQuit()
#                checkQuit()
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
