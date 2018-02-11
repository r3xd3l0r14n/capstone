"""Class that will hold logic to run the game"""

import sys

class PlayGoFish(object):
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        #create 3 players and add to a list
        self.player = [Player(self.deck), Player(self.deck), Player(self.deck)]

    """Method that runs the gaming algorithm to run through a game of Go Fish"""
    def play(self):
        print(self.deck)

        #loop through each player and have them dray 5 cards
        for i in range(5):
            for p in self.player:
                p.draw(0)

        #sort players hands
        self.sortCards()

        #check for any lucky books from initial 5 cards
        for p in self.player:
            p.bookCheck()

        turn = 0

        """Loop to control a players turn. Will remain true as long as a player correctly asks another player
            for a card AND as long as they have cards in their hand (will be true as long as the deck has cards)"""
        while self.endOfPlayCheck():
            print('\nTurn %d (%s:%d %s:%d %s:%d) %d cards remaining.' % (turn, self.player[0].name,
                                                                         self.player[0].score, self.player[1].name,
                                                                         self.player[1].score, self.player[2].name,
                                                                         self.player[2].score, self.deck.numCards()))

            whoseTurn = turn % 3

            while True:
                if self.player[whoseTurn].numCards() == 0:
                    break

                self.showHands()

                #player will decide which other player to ask a card from
                otherPlayer = self.getPlayer(self.player[whoseTurn])

                #player will decide what card they want to request
                cardFished = self.player[whoseTurn].makeTurn()

                """result will be false if player does not have card requested or
                    will contain all the cards of the same rank requested from the other player"""
                result = self.player[otherPlayer].fishFor(cardFished)

                #if player didn't get a card, draw and end turn
                if not result:
                    self.player[whoseTurn].draw(1)
                    self.sortCards()
                    break

                #add cards received to players hand
                self.player[whoseTurn].gotCards(result)
                self.sortCards()

            turn += 1

        #print winner based on player points
        if self.player[0].score == self.player[1].score == self.player[2].score:
            print('draw')
        elif self.player[0].score > (self.player[1].score & self.player[2].score):
            print(self.player[0].name, 'won!')
        elif self.player[1].score > (self.player[0].score & self.player[2].score):
            print(self.player[1].name, 'won!')
        else:
            print(self.player[2].name, 'won!')

    """Method to print each players hand (for testing purposes)"""
    def showHands(self):
        for p in self.player:
            print(p.name + "(" + str(p.score) + "): " + str(p.printHand()))

    """Method that will return which player the current player wants to ask a card from"""
    def getPlayer(self, currentPlayer):
        notFound = True
        index = -1

        #will continue to ask for a player if they do not enter a valid input
        while notFound:
            name = input(
                '\nPlayer ' + currentPlayer.name + ', which player would you like to ask a card from or "quit" to exit: ' + self.listPlayers(
                    currentPlayer) + ': ').strip()

            if name == 'quit':
                sys.exit(0)

            i = 0;

            while i < len(self.player):
                if (self.player[i] != currentPlayer) & (self.player[i].name == name):
                    index = i
                    notFound = False
                    break
                i += 1

            if notFound:
                print('Invalid player selected. Please try again')

        return index

    """Method to return all player names (for testing purposes)"""
    def listPlayers(self, currentPlayer):
        names = "Players: "
        for p in self.player:
            if currentPlayer.name != p.name:
                names += p.name + " "
        return names

    """Method to sort each player's hand"""
    def sortCards(self):
        for p in self.player:
            p.sortCards()

    """Method to check if turn is over. True if player has no cards or deck is empty"""
    def endOfPlayCheck(self):
        return (self.deck.numCards() or self.player[0].numCards() or self.player[1].numCards() or self.player[
            2].numCards())
