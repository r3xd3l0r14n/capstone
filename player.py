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


    def checkHand(self, rank):
        return self.hand.checkCards(rank)

    def toString(self):
        return self.name, self._id
    
    def matchCheck(self):
        return self.hand.bookCheck()
    
    def removeMatch(self, card):
        return self.hand.removeCards(card)
    
    # true/false check for four of a kind
    def fourKind(self):
        ranks = []
        books = []
        i = 0
        while i < len(self.hand):
            if self.hand[i] not in ranks:
                ranks.append(self.hand[i])
                if self.hand.count(self.hand[i]) == 4:
                    return True
                else:
                    return False
