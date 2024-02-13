from gameClass import *
from cardClass import *

def getDealerCard(current_deck: gameCard)-> gameCard:
    card = current_deck.gameDeck.pop()
    current_deck.dealerSum += Card.getCardValue(card)
    if Card.isAce(card): current_deck.dealerAceCount += 1
    current_deck.dealerHand.append(card)
    return current_deck

def reduceDealerAce(current_deck: gameCard)-> int:
    while current_deck.dealerSum > 21 and current_deck.dealerAceCount > 0:
        current_deck.dealerSum -= 10
        current_deck.dealerAceCount -= 1
    return current_deck.dealerSum