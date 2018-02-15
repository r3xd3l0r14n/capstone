"""Class that will contain a player's hand represented by a list of cards they have"""

class Hand(object):

	def __init__(self, deck):
		#list containing the cards in the player's hand
		self.hand = []
		#each player will be share a deck object
		self.deck = deck

	"""Method to add a card to the player's hand"""
	def addCard(self, card):
		self.hand.append(card)

	"""Method to remove call cards of a specific rank from a player's hand and return them to the other player"""
	def removeCards(self, card):
		#list of cards that are being removed
		cards = []
		i = 0

		#loop through cards in hand
		while i < self.numCards():
			#if rank of card in hand is equal to rank of card to be removed
			#remove them from current player's hand and add them to the list
			if card == Card.rank_names[self.hand[i].rank]:
				cards.append(self.hand.pop(i))

				#if a card was found, you need to decrement by 1 to account for the card removed
				i -= 1
			i += 1

		return cards

	"""Method to return the number of cards in the player's hand"""
	def numCards(self):
		return len(self.hand)

	"""Method to return player's hand as a list of card objects"""
	def getHandList(self):
		return self.hand

	"""Method to return the player's complete hand (a dict of string representation of the cards)"""
	def getHandDict(self):
		hand = []
		for h in self.hand:
			hand.append(str(h))
		return dict(enumerate(hand))

	"""Method to return a single string that represents the player's complete hand"""
	def printHand(self):
		res = []
		for h in self.hand:
			res.append(str(h))
		return res

	"""Method to check if a player's hand has a specific rank, true if found, false if not"""
	def checkCards(self, rank):
		i = 0
		found = False
		while i < self.numCards():
			if rank == Card.rank_names[self.hand[i].rank]:
				found = True
				break
			i += 1

		return found

	"""Method to sort hand by card ranks"""
	def sortHand(self):
		self.hand.sort()

	"""Method to return any books (4 of the sane rank) in the player's hand"""
	def bookCheck(self):
		#list that will contain card ranks
		ranks = []
		#list that will contain book ranks if player has any
		books = []

		i = 0
		#loop through player's hand
		while i < len(self.hand):
			#if current card rank is not in rank list, add it and proceed to check for books
			if self.hand[i] not in ranks:
				ranks.append(self.hand[i])

				#if hand has 4 of the same book, add card(only 1 needed) to book list and remove from hand
				if self.hand.count(self.hand[i]) == 4:
					books.append(self.hand[i])

					#loop through hand to remove the 4 cards of the same ranks
					j = 0
					card = self.hand[i]
					while j < 4:
						self.hand.remove(card)
						j += 1

			i += 1

		return books