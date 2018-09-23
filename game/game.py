import random as rnd

class card:
    def __init__(self,colour,rank):
        self.colour=colour
        self.rank=rank
        self.show=str(self.colour)+str(self.rank)

class deck:
    def __init__(self):
        self.iDeck={"D":["2","3","4","5","6","7","8","9","10","J","Q","K","A"],"C":["2","3","4","5","6","7","8","9","10","J","Q","K","A"],"H":["2","3","4","5","6","7","8","9","10","J","Q","K","A"],"S":["2","3","4","5","6","7","8","9","10","J","Q","K","A"]}

    def withDrawCard(self):
        suite=["D","C","H","S"]
        rnd.shuffle(suite)
        colour=suite[0]
        rnd.shuffle(self.iDeck[colour])
        rank=self.iDeck[colour][0]
        carte=card(colour,rank)
        self.iDeck[carte.colour].remove(carte.rank)

        return carte

    def removeCardFromDeck(self,carte):
        self.iDeck[carte.colour].remove(carte.rank)


class dealer:
    def __init__(self,nbPlayers):
        self.nbPlayers=nbPlayers
        self.jeu=deck()

    def cardDistribution(self):
        playerHands=[]
        for i in range(0,self.nbPlayers):
            playerHands.append(self.jeu.withDrawCard().show)

        for i in range(0, self.nbPlayers):
            playerHands[i]+=self.jeu.withDrawCard().show

        return playerHands

    def flop(self):
        board=[]
        for i in range(0,3):
            board.append(self.jeu.withDrawCard().show)

        return board

    def turn(self):
        return self.jeu.withDrawCard().show

    def river(self):
        return self.jeu.withDrawCard().show

class game:
    def __init__(self,nbPlayers):
        self.nbPlayers=nbPlayers
        self.dealer=dealer(self.nbPlayers)
        self.playerHands=self.dealer.cardDistribution()
        self.flop=self.dealer.flop()
        self.turn=self.dealer.turn()
        self.river=self.dealer.river()


