class basecard(object):
    def __init__(self, color, value):
        self.height = 5
        self.width = 3
        self.color = color
        self.value = value

    def card_info(self):
        print "Card Dimensions are " + str(self.height) + "inches x " + str(self.width) + "inches"

class unocard(basecard):
    def __init__(self, color="black", value="Draw 4"):
        super(unocard, self).__init__(color, value)
        self.face = "Uno"

    def card_info(self):
        print "Card Dimensions are " + str(self.height) + "inches x " + str(self.width) + "inches"

class playingcard(basecard):
    def __init__(self, suit=None, value=None):
        color = None
        if(suit == "Hearts" or suit == "Diamonds"):
            suit_color = "red"
        elif(suit == "Clubs" or suit == "Spades"):
            suit_color = "black"
        super(playingcard, self).__init__(suit_color, value)
        self.suit = suit
        
    def card_info(self):
        print "Playing card is the " + str(self.value) + " of " + str(self.suit)
        return self

card1 = playingcard("Clubs", 3)
card1.card_info()
print card1.suit
print card1.value
print card1.color
