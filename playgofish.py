import sys
class PlayGoFish(object):
    def __init__(self):
        self.deck = Deck()
        # self.deck.shuffle()
        self.player = [Player(self.deck), Player(self.deck), Player(self.deck)]

    def play(self):
        print(self.deck)

        for i in range(16):
            for p in self.player:
                p.draw(0)

        self.sortCards()

        for p in self.player:
            p.bookCheck()

        turn = 0

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

                otherPlayer = self.getPlayer(self.player[whoseTurn])
                cardFished = self.player[whoseTurn].makeTurn()
                result = self.player[otherPlayer].fishFor(cardFished)

                if not result:
                    self.player[whoseTurn].draw(1)
                    self.sortCards()
                    break

                self.player[whoseTurn].gotCards(result)
                self.sortCards()

            turn += 1

        if self.player[0].score == self.player[1].score == self.player[2].score:
            print('draw')
        elif self.player[0].score > (self.player[1].score & self.player[2].score):
            print(self.player[0].name, 'won!')
        elif self.player[1].score > (self.player[0].score & self.player[2].score):
            print(self.player[1].name, 'won!')
        else:
            print(self.player[2].name, 'won!')

    def showHands(self):
        for p in self.player:
            print(p.name + "(" + str(p.score) + "): " + str(p.printHand()))

    def getPlayer(self, currentPlayer):
        notFound = True
        index = -1
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

    def listPlayers(self, currentPlayer):
        names = "Players: "
        for p in self.player:
            if currentPlayer.name != p.name:
                names += p.name + " "
        return names

    def sortCards(self):
        for p in self.player:
            p.sortCards()

    def endOfPlayCheck(self):
        return (self.deck.numCards() or self.player[0].numCards() or self.player[1].numCards() or self.player[
            2].numCards())
