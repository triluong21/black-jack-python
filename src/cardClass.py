
from gamesVariables import *

class Card: 
    def __init__(self, cardValue, cardType) -> None:
        self.cardValue = cardValue
        self.cardType = cardType

    def cardValueDashType(cardValue, cardType) -> str:
        return cardValue + "-" + cardType
    
    def getCardValue(cardValue) -> int:
        if cardValue[0] in CARDPICTUREVALUES:
            if cardValue[0] == ACECARD:
                return 11
            return 10    
        
        if cardValue.find("-") == 2:
            return 10
        
        return int(cardValue[0])
    
    def isAce(cardValue) -> bool:
        if cardValue[0] == ACECARD:
            return True
        return False

