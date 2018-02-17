import json
from player import Player
from deck import Deck

class Game:

    def __init__(self):
        self._last_id = 0
        self._players = {}
        self.deck = Deck()

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

    def init_game(self): # first_ply):
        i = 1
        if self.checkEnoughPlayers():
            self.deck.shuffle()
            hands = self.deck.dealHands()
            while i <= len(self._players):
                self._players[i].hand = hands[i]
                i += 1
            rtnMsg = {'Deck' : self.deck.getDeck(), 'Hands': [self._players[1].hand.getHandDict()]}
        else:
            rtnMsg = "Failure not enough Players" 
        return rtnMsg

    def checkEnoughPlayers(self):
        if len(self._players) >= 1:
            msg = True
        else:
            msg = False
        return msg
    
    def whoFirst(self):
        who_list = [x for x in self._players]
        num_of_players = len(self._players)
        return who_list[random.randrage(0, num_of_players)]
    
    def turn_update(self, turn):
        rtnMsg = {'Turn' : self._players[turn]}
        return rtnMsg
    
    def checkEnd(self):
        
    
    def game_loop(self):
        self.init_game()
        turn = self.whoFirst()
        last_person = len(self._players)
        # create a checkEnd()
        checkQuit() # create a checkQuit()
        while self.checkEnd():
            while True:
                if turn < last_person:
                    turn_update(turn)
                    checkQuit()
                    '''
                    Need to discuss with Colin about what information will
                    be returned from clicks
                    
                    if event.type == mouseClick:
                        if position IVO of x:
                            opponent = joe1
                        elif position IVO of y:
                            opponent = joe2
                        else:
                            if card.clicked(position):
                                call a func to return selected card value
                                matches = checkMatches(blah)
                                if matches[0] != '':
                                        for match in matches:
                                            PLAYERHAND.addCard(match)
                                            HANDS[opponent1].removeCard(match)
                                            fk = fourKind(PLAYERHAND)
                                            print(fk)
                                            if fk:
                                                SCORES[turn] += 1
                                else:
                                    checkQuit()
                                    turn += 1
                                    if self.deck.numCards() > 0:
                                        player.draw()
                                    checkFourKind(player hand)
                                    if checkFourKind:
                                        SCORES[turn] += 1
                                    checkIfWon()
                                    
                else:
                    turn_update(turn)
                    checkQuit()
                    if event.type == mouseClick:
                        if position IVO of x:
                            opponent = joe1
                        elif position IVO of y:
                            opponent = joe2
                        else:
                            if card.clicked(position):
                                call a func to return selected card value
                                matches = checkMatches(blah)
                                if matches[0] != '':
                                        for match in matches:
                                            PLAYERHAND.addCard(match)
                                            HANDS[opponent1].removeCard(match)
                                            fk = fourKind(PLAYERHAND)
                                            print(fk)
                                            if fk:
                                                SCORES[turn] += 1
                                else:
                                    checkQuit()
                                    turn = 1
                                    if self.deck.numCards() > 0:
                                        player.draw()
                                    checkFourKind(player hand)
                                    if checkFourKind:
                                        SCORES[turn] += 1
                                    checkIfWon()
                                    '''
        
    