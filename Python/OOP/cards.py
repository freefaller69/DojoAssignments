class basecard(object):
    def __init__(self, value, color):
        self.height = 5
        self.width = 3
        self.color = color
        self.value = value


class playingcard(basecard):
    def __init__(self, suit, color=None, value=None):
        super(playingcard, self).__init__(color, value)
        self.suit = suit
    def check_color(self):
        if(self.suit == "Hearts" or self.suit == "Diamonds"):
            self.color = "red"
        elif(self.suit == "Clubs" or self.suit == "Spades"):
            self.color = "black"
        else:
            self.color = "None"
        print self.color, self.suit, self.value

card1 = playingcard("Clubs", 3)
card1.check_color()
