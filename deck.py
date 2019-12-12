from card import *
import random

class deck:
    cards=[]
    def __init__ (self):
        for i in ["Diamonds", "Spades", "Clubs", "Hearts"]:
            for j in range(2, 16):  # 15 signifies penalty card.
               self.cards.append(card(j,i))
        self.shuffle()
                
    def shuffle(self):
        self.shuffled_list=[]
        while len(self.cards)>0:
            rand_card_index=random.randrange(0,len(self.cards))
            self.shuffled_list.append(self.cards.pop(rand_card_index))
        self.cards=self.shuffled_list

    def draw(self):
        return self.cards.pop()



