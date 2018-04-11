"""This class will contain the deck of cards represented by a list of card objects"""
from card import Card
from hand import Hand
import random


class Deck(object):

    def __init__(self):
        # list of card objects
        self.cards = []
        # for loop to initialize 52 cards with proper ranks and suits
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    """String method to return a string representation of all
        the cards in the deck"""

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    """Method to remove top card from deck, called when players draw"""

    def drawCard(self, i=-1):
        return self.cards.pop(i)

    """Method to shuffle the deck of cards"""

    def shuffle(self):
        random.shuffle(self.cards)

    """Method to sort the cards in order of rank (uses the rich comparison methods
        in the card class"""

    def sort(self):
        self.cards.sort()

    """Method to return the number of cards left in the deck"""

    def numCards(self):
        return len(self.cards)

    """Method to return a dictionary with keys from 0-51 with the values being
        the string representation of each card in the deck"""

    def getDeck(self):
        deck = []
        for c in self.cards:
            deck.append(str(c))

        # convert list of string representation of cards in the deck into a dictionary
        return dict(enumerate(deck))

    def dealHands(self, num):
        h = 1
        hands = [Hand(), Hand(), Hand(), Hand()]
        print(num)
        while h <= num:
            for i in range(5):
                hands[h].addCard(self.drawCard())
            h += 1
        return hands
