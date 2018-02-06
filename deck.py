import random

class Deck(object):
	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1, 14):
				card = Card(suit, rank)
				self.cards.append(card)

	def __str__(self):
		res = []
		for card in self.cards:
			res.append(str(card))
		return '\n'.join(res)

	def pop_card(self, i=-1):
		return self.cards.pop(i)

	def shuffle(self):
		random.shuffle(self.cards)

	def sort(self):
		self.cards.sort()

	def numCards(self):
		return len(self.cards)

	def getDeck(self):
		deck =[]
		for c in self.cards:
			deck.append(str(c))
		return dict(enumerate(deck))