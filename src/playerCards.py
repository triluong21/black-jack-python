from cardClass import *
from gameClass import *

def getPlayerCard(current_deck: gameCard)-> gameCard:
    card = current_deck.gameDeck.pop()
    current_deck.playerSum += Card.getCardValue(card)
    if Card.isAce(card): current_deck.playerAceCount += 1
    current_deck.playerHand.append(card)
    return current_deck

def reducePlayAce(current_deck: gameCard)-> int:
    while current_deck.playerSum > 21 and current_deck.playerAceCount > 0:
        current_deck.playerSum -= 10
        current_deck.playerAceCount -= 1
    return current_deck.playerSum
