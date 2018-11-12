from flask_sqlalchemy import SQLAlchemy

import random # for cards


db = SQLAlchemy()


#class to represrent playing card
class Card(object):

    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                 "Jack", "Queen", "King"]
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    # rich comparison method
    def __lt__(self, other):
        if self.suit < other.suit:
            return True
        elif self.suit > other.suit:
            return False
        else:
            return self.rank < other.rank

#class to represent deck of playing cards
class Deck(object):

    def __init__(self):
        self.cards = [] #card arry
        for suit in range(4):
            for rank in range(1,14):
                card = Card(rank, suit) #create a card
                self.cards.append(card) #add it to the array

    #i = 0 would be the bottom card of the deck, so top is -1
    def remove_card(self, i=-1):
        return self.cards.pop(i)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()
