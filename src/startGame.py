from cardClass import * 
from dealerCards import *
from playerCards import *
from buildCardImg import *
import tkinter as tk 
from tkinter import ttk



def startGame(current_deck: gameCard) -> int:
    # Setup window
    window = tk.Tk()
    window.geometry('800x400')
    window.title("Black Jack Game")

    dealer_card_list = getImglist(current_deck.dealerHand) 
    for i in range(len(dealer_card_list)):
        if i == 0:
            hiddenCard = hiddenCardImg()
            lable = ttk.Label(window, text="", image=hiddenCard[0])
        else:
            lable = ttk.Label(window, text="", image=dealer_card_list[i])
        display_column = i + 1
        lable.grid(row= 1, column= display_column)
        
    player_card_list = getImglist(current_deck.playerHand)
    for i in range(len(player_card_list)):
        lable = ttk.Label(window, text="", image=player_card_list[i])
        display_column = i + 1
        lable.grid(row= 2, column= display_column)

    
    def additionalCard():
        # Draw additional card for player 
        getPlayerCard(current_deck)
        # Check points
        if reducePlayAce(current_deck) > 21:
            hitButton.config(state='disabled')
        # Redisplay cards    
        dealer_card_list = getImglist(current_deck.dealerHand) 
        for i in range(len(dealer_card_list)):
            if i == 0:
                hiddenCard = hiddenCardImg()
                lable = ttk.Label(window, text="", image=hiddenCard[0])
            else:
                lable = ttk.Label(window, text="", image=dealer_card_list[i])
            display_column = i + 1
            lable.grid(row= 1, column= display_column)
            
        player_card_list = getImglist(current_deck.playerHand)
        for i in range(len(player_card_list)):
            lable = ttk.Label(window, text="", image=player_card_list[i])
            display_column = i + 1
            lable.grid(row= 2, column= display_column)
        
        window.mainloop()

    def stayWithCard(): 
        hitButton.config(state='disabled')
        stayButton.config(state='disabled')

        # Draw additional card for Dealer ONLY when Player sum < 22
        if reducePlayAce(current_deck) <= 21:
            while reduceDealerAce(current_deck) < 17:
                getDealerCard(current_deck)

        # Redisplay cards    
        dealer_card_list = getImglist(current_deck.dealerHand) 
        for i in range(len(dealer_card_list)):
            lable = ttk.Label(window, text="", image=dealer_card_list[i])
            display_column = i + 1
            lable.grid(row= 1, column= display_column)
            
        player_card_list = getImglist(current_deck.playerHand)
        for i in range(len(player_card_list)):
            lable = ttk.Label(window, text="", image=player_card_list[i])
            display_column = i + 1
            lable.grid(row= 2, column= display_column)
        
        # Display label anounces Who wins?
        announceMessage = str
        if current_deck.playerSum > 21:
            announceMessage = "You Lose!"
        elif current_deck.dealerSum > 21:
            announceMessage = "You Win!"
        elif current_deck.playerSum == current_deck.dealerSum:
            announceMessage = "Tie!"
        elif current_deck.playerSum > current_deck.dealerSum:
            announceMessage = "You Win!"
        elif current_deck.playerSum < current_deck.dealerSum:
            announceMessage = "You Lose!"

        lable = ttk.Label(window, text=announceMessage, font=("Arial", 15))
        lable.grid(row=3, column=3)

        window.mainloop()    

    def quitPlaying():
        window.destroy()

    # buttons
    hitButton = ttk.Button(window, text="Hit", command=additionalCard)
    hitButton.grid(row=3, column=1)
    stayButton = ttk.Button(window, text="Stay", command=stayWithCard)
    stayButton.grid(row=3, column=2)
    quitButton = ttk.Button(window, text="Quit", command=quitPlaying)
    quitButton.grid(row=4, column=1, columnspan=2)


# run
    window.mainloop()

