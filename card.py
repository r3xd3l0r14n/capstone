"""This class will hold the attributes for a card object including its rank and suit"""

class Card(object):

	#list of suit names
	suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
	#list of rank names
	rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7",
				  "8", "9", "10", "Jack", "Queen", "King"]

	def __init__(self, suit=0, rank=2):
		self.suit = suit
		self.rank = rank

	"""String method to return a string representation of a card object"""
	def __str__(self):
		return '%s of %s' % (Card.rank_names[self.rank],
							 Card.suit_names[self.suit])

	"""Rich comparison method to check if a card object is less than another card object
		based on its rank value"""
	def __lt__(self, other):
		return self.rank < other.rank

	"""Rich comparison method to check if a card object is equal to another card object
		based on its rank value"""
	def __eq__(self, other):
		return self.rank == other.rank