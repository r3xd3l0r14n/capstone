class Hand(object):
	def __init__(self, deck):
		self.hand = []
		self.deck = deck

	def addCard(self, card):
		self.hand.append(card)

	def removeCards(self, card):
		cards = []
		i = 0

		while i < self.numCards():
			if card == Card.rank_names[self.hand[i].rank]:
				cards.append(self.hand.pop(i))
				i -= 1
			i += 1

		return cards

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
				break
			i += 1

		return found

	def sortHand(self):
		self.hand.sort()

	def bookCheck(self):
		ranks = []
		books = []

		i = 0
		while i < len(self.hand):
			if self.hand[i] not in ranks:
				ranks.append(self.hand[i])
				if self.hand.count(self.hand[i]) == 4:
					books.append(self.hand[i])

					j = 0
					card = self.hand[i]
					while j < 4:
						self.hand.remove(card)
						j += 1

			i += 1

		return books