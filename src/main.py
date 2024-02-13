from startGame import *
from dealerCards import *
from playerCards import *
from buildDeck import *


def main():
    # Build new deck of Card
    current_deck = buildDeck()

    # Hidden card for Dealer
    getDealerCard(current_deck)
    # Second card for Dealer
    getDealerCard(current_deck)

    print(current_deck.dealerHand)
    print(current_deck.dealerSum)
    print(current_deck.dealerAceCount)

    # Player two cards
    getPlayerCard(current_deck)
    getPlayerCard(current_deck)
    print(current_deck.playerHand)
    print(current_deck.playerSum)
    print(current_deck.playerAceCount)

    # Get to Play now
    stillPlaying = startGame(current_deck)
    print(stillPlaying)

if __name__ == "__main__":   
    main()


