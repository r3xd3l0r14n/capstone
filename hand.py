class Hand:

    def __init__(self, deck):
        self.hand = []
        self.deck = deck

    def addCard(self, card):
        self.hand.append(card)

    def removeCard(self, card):
        self.hand.remove(card)

    def numCards(self):
        return len(self.hand)

    def getHand(self):
        return self.hand

    def printHand(self):
        res = []
        for h in self.hand:
            res.append(str(h))
        return res

    def checkCards(self, rank):
        i = 0
        found = False
        while i < self.numCards():
            if rank == Card.rank_names[self.hand[i].rank]:
                found = True
            i += 1

        return found
