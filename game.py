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
        # self.player = Player()
        self.scores = {}

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
        for score in self._players:
            self.scores[score] = 0
        if self.checkEnoughPlayers():
            self.deck.shuffle()
            hands = self.deck.dealHands(len(self._players))
            rtnMsg = {'Deck': self.deck.getDeck(), 'Hands': {}}
            while i <= len(self._players):
                self._players[i].hand = hands[i]
                rtnMsg['Hands'][i] = (self._players[i].hand.getHandDict())
                i += 1
                # print(rtnMsg)
        else:
            rtnMsg = {'msg': 'Failure to start game, not enough players'}
        return rtnMsg

    def checkEnoughPlayers(self):
        if len(self._players) >= 1:
            msg = True
        else:
            msg = False
        return msg

    # I believe i correctly changed this to return the input from user
    def stripMsg(self, msg):
        nMsg = msg['card']
        return nMsg

    #    def turn_update(self, turn):
    #        rtnMsg = {'Turn': self._players[turn]._id}
    #        return rtnMsg

    def updateGame(self, card):
        # print('The card that was fished for was %s' % card)
        return True

    def newUpdateGame(self):  # first_ply):
        i = 1
        rtnMsg = {'Deck': self.deck.getDeck(), 'Hands': {}, 'Scores': self.scores}
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
        # scores = {}
        last_person = len(self._players)
        strip = self.stripMsg(msg)
        card = Card("temp", int(strip))
        currentPlayer = self._players[turn]

        """should make it so its based on number of players and not static 4"""
        if (currentPlayer._id + 1) <= len(self._players):
            opponent = self._players[turn + 1]
        else:
            opponent = self._players[1]

        if self.updateGame(card):

            """Currently checks if card player requested is in their hand, if it's not it will skip their turn for now. 
                May be updated in future to loop so that user enters correct data"""
            # if currentPlayer.checkHand(card):
            if opponent.checkHand(card):
                # removes cards from opponent's hand, and returns them in a list
                cardAdded = opponent.removeMatch(card)
                # loop through list of cards, and add to current player's hand
                # count = 0
                # while count < len(cardAdded):
                #     currentPlayer.hand.addCard(cardAdded(count))
                for x in cardAdded:
                    currentPlayer.hand.addCard(x)
                fourKind = currentPlayer.fourKind()
                print(fourKind)
                if fourKind[0] == True:
                    self.scores[currentPlayer._id] += 1
                    cardRemoved = currentPlayer.removeMatch(fourKind[1])
                    print(self.scores)
            else:
                print(turn)
                if self.deck.numCards() > 0:
                    currentPlayer.hand.addCard(self.deck.drawCard())
                fourKind = currentPlayer.fourKind()
                print(fourKind)
                if fourKind[0] == True:
                    self.scores[currentPlayer._id] += 1
                    cardRemoved = currentPlayer.removeMatch(fourKind[1])
                    print(self.scores)

        return self.newUpdateGame()


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
