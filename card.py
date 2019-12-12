class card:
    values=None
    suits=None
    def __init__ (self, value, suit):
        self.values=value
        self.suits=suit


    def show_card(self):
        if self.values==15:
            return "Penalty Card"
        elif self.values==14:
            return "Ace of {}".format(self.suits)
        elif self.values==13:
            return "King of {}".format(self.suits)
        elif self.values==12:
            return "Queen of {}".format(self.suits)
        elif self.values==11:
            return "Jack of {}".format(self.suits)
        else:
            return "{} of {}".format(self.values,self.suits)

