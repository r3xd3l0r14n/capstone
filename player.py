import sys

class Player(object):
	def __init__(self, deck):
		self.hand = Hand(deck)
		self.book = []
		self.deck = deck
		self.score = 0
		self.name = input('Name Yourself: ').strip()

	def draw(self, val):
		cardDrawn = self.deck.pop_card()
		self.hand.addCard(cardDrawn)
		print('\n%s drew %s.' % (self.name, cardDrawn))

		if val == 1:
			self.bookCheck()

	def numCards(self):
		return self.hand.numCards()

	def printHand(self):
		return self.hand.printHand()

	def checkHand(self, rank):
		return self.hand.checkCards(rank)

	def emptyCheck(self):
		if self.numCards() == 0 and self.deck.numCards() > 0:
			self.draw(1)

	def sortCards(self):
		self.hand.sortHand()

	def makeTurn(self):
		while True:
			print ('\n%s\'s hand: %s' % (self.name,self.printHand()))
			chooseCard = input('What card do you ask for? (Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King or "quit" to exit): ')
			if chooseCard == 'quit':
				sys.exit(0)
			elif chooseCard not in Card.rank_names:
				print ("\nInvalid Selection! Try Again")
			elif not self.checkHand(chooseCard):
				print ("\nYou don\'t have that card. Try again!")
			else:
				return chooseCard

	def fishFor(self, rank):
		if self.checkHand(rank):
			a = self.hand.removeCards(rank)
			self.emptyCheck()
			return a
		else:
			return False

	def gotCards(self, cards):
		rank = Card.rank_names[cards[0].rank]
		i = len(cards)
		j = 0

		while j < i:
			self.hand.addCard(cards[j])
			j += 1

		print('\n%s got %d more %s.' % (self.name, len(cards), rank))

		self.bookCheck()

	def bookCheck(self):
		books = self.hand.bookCheck()
		res = []


		if len(books) > 0:
			self.score += len(books)
			books.sort()

			res.append('\nPlayer ' + self.name + ' has completed the following books:')

			i = 0
			while i < len(books):
				res.append(Card.rank_names[books[i].rank])
				i += 1

			newStr = " ".join(res)

			print(newStr)

		self.emptyCheck()