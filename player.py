"""Class that will define a player and all their attributes"""
import sys

class Player(object):
	def __init__(self, deck):
		#object representing the player's hand
		self.hand = Hand(deck)
		#list that will contain books the player completed
		self.book = []
		#each player will share the deck object
		self.deck = deck
		#score based on how many books they have
		self.score = 0
		#holds the player's name
		self.name = input('Name Yourself: ').strip()

	"""Method for a player to draw a card from the deck and add it to their hand"""
	def draw(self, val):
		cardDrawn = self.deck.pop_card()
		self.hand.addCard(cardDrawn)
		print('\n%s drew %s.' % (self.name, cardDrawn))

		#if val = 1, will check for books after drawing
		if val == 1:
			self.bookCheck()

	"""Method that returns the number of cards in a player's hand"""
	def numCards(self):
		return self.hand.numCards()

	"""Method to return a single string that represents the player's complete hand"""
	def printHand(self):
		return self.hand.printHand()

	"""Method to check if a player's hand has a specific rank, true if found, false if not"""
	def checkHand(self, rank):
		return self.hand.checkCards(rank)

	"""Method to check if a player's hand is empty, if true and deck still has cards, player will draw 1"""
	def emptyCheck(self):
		if self.numCards() == 0 and self.deck.numCards() > 0:
			self.draw(1)

	"""Method to sort a player's hand by card ranks"""
	def sortCards(self):
		self.hand.sortHand()

	"""Method that contains logic for a player to choose what card they'd like to request from another player (returns chosen rank)"""
	def makeTurn(self):
		#will loop until player provides correct input (valid rank AND player must have that rank in their hand
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

	"""Method to check player's hand for requested card, returns all available cards of rank requested in a list if found, false if not"""
	def fishFor(self, rank):
		#check if rank is in player's hand
		if self.checkHand(rank):
			#if found, remove all cards from player's hand and add to list that will be returned
			a = self.hand.removeCards(rank)
			#check if players hand is empty after card removal
			self.emptyCheck()
			return a
		else:
			return False

	"""Method that will add that were requested by the player to their hand"""
	def gotCards(self, cards):
		rank = Card.rank_names[cards[0].rank]
		i = len(cards)
		j = 0

		while j < i:
			self.hand.addCard(cards[j])
			j += 1

		print('\n%s got %d more %s.' % (self.name, len(cards), rank))

		#check if player completed a book after receiving cards
		self.bookCheck()

	"""Method to check player's hand for any books"""
	def bookCheck(self):
		#list that will contain books completed or be empty if no books were completed
		books = self.hand.bookCheck()
		#string that will print what books were completed if any
		res = []

		#if length of list is greater than 1, a book was completed
		if len(books) > 0:
			self.score += len(books)
			books.sort()

			res.append('\nPlayer ' + self.name + ' has completed the following books:')

			i = 0
			while i < len(books):
				#add rank to player's list of completed books
				self.book.append(Card.rank_names[books[i].rank])
				#add rank to string that will print what book the player currently completed
				res.append(Card.rank_names[books[i].rank])
				i += 1

			newStr = " ".join(res)

			print(newStr)

			#check if player's hand is empty after completing a book
			self.emptyCheck()

	"""Method to print every book a player completed, or none if none were completed"""
	def printBooks(self):
		#string to hold representation of books completed or none if no books are completed
		res = []

		#if player's score is greater than 0, they completed a book
		if self.score > 0:
			i = 0

			while i < len(self.book):
				res.append(self.book[i])
				i += 1

			return res
		else
			res = res.append('None')
			return res