from gameClass import *
from cardClass import *
from gamesVariables import *
import random


def buildDeck()-> gameCard:
    deck = []
    parameters = gameCard()

    # Build new deck of cards
    for i in range(len(CARDVALUES)):
        for j in range(len(CARDTYPES)):
            card = Card.cardValueDashType(CARDVALUES[i], CARDTYPES[j])
            deck.append(card)

    # Shuffle cards
    random.shuffle(deck)

    parameters.dealerSum = 0
    parameters.dealerAceCount = 0
    parameters.dealerHand = []
    parameters.playerSum = 0
    parameters.playerAceCount = 0
    parameters.playerHand = []
    parameters.gameDeck = []
    parameters.gameDeck = deck
    return parameters
