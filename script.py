import random

# a Card has the following
#   rank
#   suit
# a Card can be shown
class Card:
    def __init__(self, rank, suit, minor, orientation):
        self.rank = rank
        self.suit = suit
        self.minor = minor
        self.orientation = orientation
    
    def show(self):
        if self.minor:
            return "{} {} of {}".format(self.orientation, self.rank, self.suit)
        else: 
            return "{} {}".format(self.orientation, self.rank)
    
# a Deck has a list of Cards
# a Deck can be shuffled
# a Player can draw a Card from the top of the Deck
class Deck:
    def __init__(self, build):
        self.cards = []
        if build:
            self.buildDeck()

    def show(self):
        for card in self.cards:
            print(card.show())
    
    # for each suit, for each rank, create a card of that rank and suit
    # for major, add one of each card
    def buildDeck(self):
        self.cards = []
        # minor arcana are just ace through king for each suit
        for suit in ["Pentacles", "Swords", "Wands", "Cups"]:
            for rank in ["ace", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "page", "knight", "queen", "king"]:
                self.cards.append(Card(rank, suit, True, "upright"))
        # major arcana just have the suit as "major" and their rank is the full title of the card
        for rank in ["0 THE FOOL", "I THE MAGICIAN", "II THE HIGH PRIESTESS", "III THE EMPRESS", "IV THE EMPEROR", "V THE HIEROPHANT", "VI THE LOVERS", "VII THE CHARIOT", "VIII STRENGTH", "IX THE HERMIT", "X WHEEL OF FORTUNE", "XI JUSTICE", "XII THE HANGED MAN", "XIII DEATH", "XIV TEMPERANCE", "XV THE DEVIL", "XVI THE TOWER", "XVII THE STAR", "XVIII THE MOON", "XIX THE SUN", "XX JUDGEMENT", "XXI THE WORLD"]:
                self.cards.append(Card(rank, "major", False, "upright"))

    # default shuffle
    # plus a little spice: randomize card orientation
    def shuffle(self):
        random.shuffle(self.cards)
        for card in self.cards:
            card.orientation = random.choice(["upright", "reversed"])

    def majorSplit(self):
        aside = Deck(False)
        for card in self.cards:
            if card.suit == "major":
                aside.cards.append(card)
                self.cards.remove(card)
        return aside
    
    def combine(self, other):
        if isinstance(other, Deck):
            self.cards.append(other.cards)
        self.shuffle()

    # take card at end
    def draw(self):
        return self.cards.pop()

# a Player has the following
#   a name
#   a hand of Cards
# a Player can show their hand
class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name

    def rename(self, name):
        self.name = name
    
    def showHand(self):
        print(self.name + "'s hand contains: ")
        for card in self.hand:
            print(card.show())
    
    def show(self):
        print(self.name)
        self.showHand()
    
# # make card
# card = Card(3, "spades")
# print(card.show())

# # make deck
# deck = Deck()
# deck.show()
# print("----------------")
# # shuffle deck
# deck.shuffle()
# deck.show()
# print("----------------")
# # drawing cards
# for i in range(1,40):
#     print(deck.draw().show())
# print("----------------")
# # show remaining deck
# deck.show()

# make deck
deck = Deck(True)
deck.show()
print("----------------")
deck.shuffle()
deck.show()
print("----------------")

# create a player
player = Player("name")
player.show()
print("----------------")
# player draws three cards
for i in range(0,3):
    player.hand.append(deck.draw())
    player.show()
    print("----------------")

# split major and minor arcana
majors = deck.majorSplit()
print("----------------")
print(majors.show())
print("----------------")
print(deck.show())
print("----------------")

# draw a card from each deck
player.hand.append(deck.draw())
player.show()
print("----------------")
player.hand.append(majors.draw())
player.show()
print("----------------")

# combine two decks
deck.combine(majors.cards)
print(deck.show())
print("----------------")
