from hand import Hand
class Player:

    def __init__(self, player_id, name):#, deck):
        self._id = player_id
        self.name = name
        self.hand = Hand()  # need to discuss, we may need to pass the deck back and forth via JSON
        #self.book = []
        #self.deck = deck
        #self.score = 0


    def draw(self):
        cardDrawn = self.deck.pop_card()
        self.hand.addCard(cardDrawn)
        print('%s drew %s.' % (self.name, cardDrawn))


    def numCards(self):
        return self.hand.numCards()


    def printHand(self):
        return self.hand.printHand()


    def checkHand(self, card):
        return self.hand.checkCards(card)

    def toString(self):
        return self.name, self._id
    
    def matchCheck(self):
        return self.hand.bookCheck()
    
    def removeMatch(self, card):
        return self.hand.removeCards(card)
    
    # true/false check for four of a kind
    def fourKind(self):
        ranks = []
        rtnMsg = {0:False, 1:0}
        lark = self.hand.hand
        for i in lark:
            if i not in ranks:
                ranks.append(i)
                if lark.count(i) == 4:
                    print(True)
                    rtnMsg = {0:True, 1:i}
                #else:
                #     rtnMsg = False
        return rtnMsg
