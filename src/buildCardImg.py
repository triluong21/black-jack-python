from PIL import Image, ImageTk


def getImglist(cardHand: []) -> []:
    dealer_card_list = []
    for i in range(len(cardHand)):
    # Import an image
        my_image_path = f"./cards/{cardHand[i]}.png"
        my_image = Image.open(my_image_path).resize((110,154))
        image_tk = ImageTk.PhotoImage(my_image)
        dealer_card_list.append(image_tk)
    return dealer_card_list    

def hiddenCardImg() -> []:
    hidden_card_list = []
    # Import an image
    my_image_path = f"./cards/BACK.png"
    my_image = Image.open(my_image_path).resize((110,154))
    image_tk = ImageTk.PhotoImage(my_image)
    hidden_card_list.append(image_tk)
    return hidden_card_list 