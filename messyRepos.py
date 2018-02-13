'''
Subject to change as discussed, pushing everything I have at the moment (including the classes
that won't be used) '''

class Deck:
    def __init__(self):
        self.values = ('a', '2', '3', '4', '5', '6', '7', '8', '9',
                       '10', 'j', 'q', 'k')
        self.suits = ('clubs', 'hearts', 'spades', 'diamonds')
        self.deck = [] # Deck is a list
        for suit in self.suits:
            for value in self.values:
                self.deck.append((value, suit)) # Calls each value of each suit
        i = 0
        for acard in self.deck:
            i += 1
        random.shuffle(self.deck) # Shuffles deck

    def drawCard(self):
    # Removes a card from the deck
        return self.deck.pop(0)

    def getLen(self):
    # Gets the length of the deck
        return len(self.deck)
        
	def Deal(self):
	# Deals cards at the beginning of the game
		hand1 = [] # Creates 4 empty hands
		hand2 = []
		hand3 = []
		hand4 = []
		for i in range(5):
			hand1.append(self.drawCard()) # Draws cards for each hand
			hand2.append(self.drawCard())
			hand3.append(self.drawCard())
			hand4.append(self.drawCard())
		hands = [hand1, hand2, hand3, hand4] # Puts the four hands in a list called hands
		return hands

class Card(self):

    def getValue(self):
    # Returns the suit and value of a card
        return self.cardval

class OtherPlayer:
    global MOVES
    def __init__(self, hand, thisOther):
        self.hand = hand.getHand()
        self.handobj = hand
        self.thisOtherPlayer = thisOpponent

    def getMove(self):
        numlist = []
        cardlist = []
        if len(self.hand) == 0:
            gameWon(self.handobj) # If the number of cards in a hand is 0, the game is WON!
        if len(self.hand) == 1:
            return self.hand[0] # If there is one card in the hand, return the card
        for cardval in self.hand:
            numlist.append(cardval[0]) # Builds a list of the card values in the hand
            cardlist.append(cardval) # Creates a list of the cards and number in the hand
            
    def makePlay(self):
        self.cardvalue = self.getMove()
        self.opponentText = self.getOpponent()
        self.opponent = HANDS[self.opponentText] # Looks at the opponent's hand
        MOVES[self.thisOpponent].append(self.cardvalue[0])
        checkQuit()
        #Function for matching cards
        self.matches = checkMatch(self.opponent, self.cardvalue)
        if self.matches[0] != '': # Checks if a match was made
            for amatch in self.matches:
                self.handobj.addCard(amatch) # Add card to one players hand
                self.opponent.removeCard(amatch) # Remove card from the other players hand
                fk = fourKind(self.handobj)
                if fk:
                    SCORES[self.thisOpponent] += 1
            self.makePlay()
        else:
            checkQuit()
            if DECK.getLen() > 0:
                self.handobj.addCard(DECK.drawCard())
            fk = fourKind(self.handobj)
            if fk:
                SCORES[self.thisOpponent] += 1
            gameWon(self.handobj)
            return None        


def deleteFour(hand, cardValue):
# Deletes the four matching cards in the hand
    delList = []
    for acard in hand.getHand():
        if acard[0] == cardValue:
            delList.append(acard)
    for delCard in delList:
        hand.removeCard(delCard)

def fourKind(hand):
# Distinguishes 4 of a kind, and put them into a list
    checkinglist = []
    matchedlist = []
    fourofakind = []
    occurences = 0
    ret = False
    cards = hand.getHand()
    for acard in cards:
        checkinglist.append(acard[0])
    checkinglist.sort()
    for item in checkinglist:
        occurences = checkinglist.count(item)
        if occurences > 3:
            matchedlist.append(item)
    if len(matchedlist) > 0: # If you four of a kind, it returns true
        deleteFour(hand, matchedlist[0])
        ret = True
    return ret
    
def checkMatch(hand, cardCheck):
# Checks if cards match
    checkHand = hand.getHand()
    matches = ['']
    cardnum = cardCheck[0]
    for acard in checkHand:
        acardnum = acard[0]
        if acardnum == cardnum:
            if '' in matches:
                matches.remove('')
            matches.append(acard)
    if '' not in matches:
    return matches
    
def gameWon(hand):
    scorekeys = list(SCORES.keys())
    scorevalues = list(SCORES.values())
    if len(hand.getHand()) == 0: # If one player has 0 hands in their hand...
            winner = scorekeys[scorevalues.index(max(scorevalues))] # The winner is the person who has the highest score
            showWinner(winner)
        


class Hand:
    def __init__(self, cards):
        self.cards = cards

    def addCard(self, card):
        self.cards.append(card) # adds cards to the hand
        return self.cards

    def removeCard(self, card):
        self.cards.remove(card) # remove cards from hand
        return self.cards

    def getHand(self):
        return self.cards # gets card values for a hand

    def getLen(self):
        return len(self.cards) # gets the length of a hand
        
def updateGame():
# Shows change in players hands, etc.
    decklen = DECK.getLen()
    danielLen = danielHand.getLen() # Lenght of each of the hands
    colinLen = colinHand.getLen()
    jasonLen = JasonHand.getLen()
    caseyLen = caseyHand.getLen()
    danielHandList = danielHand.getHand()
    danielHandList.sort()
    colinHandList = colinHand.getHand()
    colinHandList.sort()
    jasonHandList = jasonHand.getHand()
    jasonHandList.sort()
    caseyHandList = caseyHand.getHand()
    caseyHandList.sort()

def whoFirst():
    first = ['Daniel','Colin','Jason','Casey']
    return first[random.randrange(0,4)]

DECK = Deck()
dealtCards = DECK.Deal()
danielHand = Hand(dealtCards[0])
colinHand = Hand(dealtCards[1])
jasonHand = Hand(dealtCards[2])
caseyHand = Hand(dealtCards[3])
HANDS = {'Daniel':danielHand, 'Colin':colinHand,
                'Jason':jasonHand, 'Casey':caseyHand}
SCORES = {'Daniel':0, 'Colin':0, 'Jason':0, 'Casey':0}
TURN = whoFirst()
Daniel = otherPlayer(danielHand, 'Daniel')
Colin = otherPlayer(colinHand, 'Colin')
Jason = otherPlayer(jasonHand, 'Jason')
MOVES = {'Daniel':[' '],'Colin':[' '], 'Jason':[' '], 'Casey':[' ']}

def main():
# This implements ALL of the functions!
    global TURN, MOVES
        while TURN == 'Casey':
            TURN = 'mine'
            updateGame()
            gameWon(caseyHand)
            checkQuit()
            while TURN == 'mine':
				if: 
				else:
							matches = checkMatch(HANDS[opponent1], acard.getValue())
							MOVES['Casey'].append(acard.getValue()[0])
							if matches[0] != '':
								for amatch in matches:
									caseyHand.addCard(amatch)
									HANDS[opponent1].removeCard(amatch)
									fk = fourKind(caseyHand)
									print(fk)
									if fk:
										SCORES['Casey'] += 1
								TURN = 'Casey'
							else:
								checkQuit()
								TURN = 'Daniel'
								if DECK.getLen() > 0:
									drawnCard = DECK.drawCard()
									caseyHand.addCard(drawnCard)
								fk = fourKind(caseyHand)
								if fk:
									SCORES['Casey'] += 1
								gameWon(caseyHand)
								updateGame()

        if TURN == 'Daniel':
            updateGame()
            checkQuit()
            
            
            TURN = 'Colin'

        if TURN == 'Colin':
            updateGame()
            checkQuit()
            
            TURN = 'Jason'

        if TURN == 'Jason':
            updateGame()
            checkQuit()
            
            TURN = 'Casey'

