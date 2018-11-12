from flask import request, g, Blueprint, render_template
from app.models import db,Deck,Card # import the db, and the models


home = Blueprint('home', __name__)

#the route function tells the app which URL to bind to the function
@home.route("/")
def index():
    sorted_deck = Deck() #create new deck object in order
    sorted_deck_draw_card = sorted_deck.remove_card()
    print("sorted_deck_draw_card"+str(sorted_deck_draw_card))

    shuffled_deck = Deck()
    shuffled_deck.shuffle()
    shuffled_deck_draw_card = shuffled_deck.remove_card()
    print("shuffled_deck_draw_card"+str(shuffled_deck_draw_card))

    #print to terminal for resting pruposes
    counter = 0
    for card in shuffled_deck.cards:
        print(shuffled_deck.cards[counter])
        counter = counter + 1


#    print("Take of the top card from the deck")
#    print(deck.remove_card()) ## pop top card from deck

    #firstDeckCard = deck.cards[0]
    #print(firstDeckCard.suit)


    # returh the three objects with home/index.html which will post the decks
    # and the cards drawn from the top of each deck
    #just return the home page
    return render_template("home/index.html")
