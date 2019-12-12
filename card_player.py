from card import *
from deck import *



def compare_cards(card_1,card_2):#Returns highest rank card from given arguments
    if card_1.values>card_2.values:
        return card_1
    elif card_1.values<card_2.values:
        return card_2
    else:
        if card_1.suits=="Spades":
            return card_1
        elif card_1.suits=="Hearts":
            if card_2.suits=="Spades":
                return card_2
            else:
                return card_1
        elif card_1.suits=="Diamonds":
            if card_2.suits=="Spades" or card_2.suits=="Hearts":
                return card_2
            else:
                return card_1
        else:
            return card_2


#Main/Driver
num_players= input("Enter the number of players (2-4):")
if num_players!="2" and num_players!="3" and num_players!="4":
    print("ERROR: Only numbers 2-4 is allowed for number of players.")
else:
    if num_players=="2":
        p1_score=0
        p2_score=0
        high_score = 0
        game_deck=deck()

        while high_score<21 or (high_score-2)<min(p1_score,p2_score):
            draw_1= input("Player 1 turn: Press d to draw card: ") 
            while draw_1!='d':
                print("Error: Unknown input entered. Please enter d to draw a card: ")
                draw_1=input()
            drawn_1=game_deck.draw()
            print("Player 1 drew {}.".format(drawn_1.show_card()))

            draw_2= input("Player 2 turn: Press d to draw card: ")
            while draw_2!='d':
                print("Error: Unknown input entered. Please enter d to draw a card: ")
                draw_2=input()
            drawn_2=game_deck.draw()
            print("Player 2 drew {}.".format(drawn_2.show_card()))
            
            if drawn_1.values==15 and drawn_2.values==15:
                if p1_score-1<0:
                    p1_score=0
                else:
                    p1_score=p1_score-1
                
                if p2_score-1<0:
                    p2_score=0
                else:
                    p2_score=p2_score-1
                
                print("No one won the round (both players drew penalty cards).")
            elif drawn_1.values==15:
                if p1_score-1<0:
                    p1_score=0
                else:
                    p1_score=p1_score-1

                p2_score=p2_score+2
                print("Player 2 won the round.")
            elif drawn_2.values==15:
                if p2_score-1<0:
                    p2_score=0
                else:
                    p2_score=p2_score-1

                p1_score=p1_score+2
                print("Player 1 won the round.")
            else:
                win_card= compare_cards(drawn_1,drawn_2)
                if win_card.values == drawn_1.values and win_card.suits == drawn_1.suits:
                    p1_score=p1_score+2
                    print("Player 1 won the round.")
                else:
                    p2_score=p2_score+2
                    print("Player 2 won the round.")

            print("Player 1 score is ",p1_score)
            print("Player 2 score is ",p2_score)
            high_score=max(p1_score,p2_score)
            game_deck.shuffle()
        
        if p1_score>p2_score:
            print("Player 1 won the game with a score of {}. Player 2's score was {}".format(p1_score,p2_score))
        else:
            print("Player 2 won the game with a score of {}. Player 1's score was {}".format(p2_score,p1_score))


    elif num_players=="3":
        p1_score=0
        p2_score=0
        p3_score=0
        high_score=0
        second_high=0
        game_deck=deck()
        num_drawn=0 # Used to account for deck running out of cards
        no_winner=0 # Used If deck runs out of cards and there is no winner.

        while high_score<21 or high_score-2<second_high:
            if num_drawn==56:
                no_winner=1
                break 
            draw_1= input("Player 1 turn: Press d to draw card: ") 
            while draw_1!='d':
                print("Error: Unknown input entered. Please enter d to draw a card: ")
                draw_1=input()
         
            drawn_1=game_deck.draw()
            num_drawn=num_drawn+1
            print("Player 1 drew {}.".format(drawn_1.show_card()))

            if num_drawn==56:
                no_winner=1
                break
            draw_2= input("Player 2 turn: Press d to draw card: ")
            while draw_2!='d':
                print("Error: Unknown input entered. Please enter d to draw a card: ")
                draw_2=input()
            drawn_2=game_deck.draw()
            num_drawn=num_drawn+1
            print("Player 2 drew {}.".format(drawn_2.show_card()))

            if num_drawn==56:
                no_winner=1
                break
            draw_3=input("Player 3 turn: Press d to draw card: ")
            while draw_3!='d':
                print("Error: Unknown input entered. Please enter d to draw a card: ")
                draw_3=input()
            drawn_3=game_deck.draw()
            num_drawn=num_drawn+1
            print("Player 3 drew {}.".format(drawn_3.show_card()))
           
            if drawn_1.values==15 and drawn_2.values==15 and drawn_3.values==15:
                if p1_score-1<0:
                    p1_score=0
                else:
                    p1_score=p1_score-1
                
                if p2_score-1<0:
                    p2_score=0
                else:
                    p2_score=p2_score-1
                
                if p3_score-1<0:
                    p3_score=0
                else:
                    p3_score=p3_score-1
                
                print("No one won the round (All players drew penalty cards).")
            elif drawn_1.values==15 and drawn_2.values==15:
                if p1_score-1<0:
                    p1_score=0
                else:
                    p1_score=p1_score-1
                if p2_score-1<0:
                    p2_score=0
                else:
                    p2_score=p2_score-1

                p3_score=p3_score+2
                print("Player 3 won the round.")
            elif drawn_1.values==15 and drawn_3.values==15:
                if p1_score-1<0:
                    p1_score=0
                else:
                    p1_score=p1_score-1
                if p3_score-1<0:
                    p3_score=0
                else:
                    p3_score=p3_score-1

                p2_score=p2_score+2
                print("Player 2 won the round.")
            elif drawn_2.values==15 and drawn_3.values==15:
                if p2_score-1<0:
                    p2_score=0
                else:
                    p2_score=p2_score-1
                if p3_score-1<0:
                    p3_score=0
                else:
                    p3_score=p3_score-1

                p1_score=p1_score+2
                print("Player 1 won the round.")
            elif drawn_1.values==15:
                if p1_score-1<0:
                    p1_score=0
                else:
                    p1_score=p1_score-1

                win_card=compare_cards(drawn_2,drawn_3)
                if win_card.values==drawn_2.values and win_card.suits == drawn_2.suits:
                    p2_score=p2_score+2
                    print("Player 2 won the round.")
                else:
                    p3_score=p3_score+2
                    print("Player 3 won the round.")
                
            elif drawn_2.values==15:
                if p2_score-1<0:
                    p2_score=0
                else:
                    p2_score=p2_score-1

                win_card=compare_cards(drawn_1,drawn_3)
                if win_card.values==drawn_1.values and win_card.suits == drawn_1.suits:
                    p1_score=p1_score+2
                    print("Player 1 won the round.")
                else:
                    p3_score=p3_score+2
                    print("Player 3 won the round.")
            elif drawn_3.values==15:
                if p3_score-1<0:
                    p3_score=0
                else:
                    p3_score=p3_score-1

                win_card=compare_cards(drawn_2,drawn_1)
                if win_card.values==drawn_1.values and win_card.suits == drawn_1.suits:
                    p1_score=p1_score+2
                    print("Player 1 won the round.")
                else:
                    p2_score=p2_score+2
                    print("Player 2 won the round.")
            else:
                win_card1= compare_cards(drawn_1,drawn_2)
                win_card=compare_cards(win_card1,drawn_3)

                if win_card.values == drawn_1.values and win_card.suits == drawn_1.suits:
                    p1_score=p1_score+2
                    print("Player 1 won the round.")
                elif win_card.values == drawn_2.values and win_card.suits == drawn_2.suits:
                    p2_score=p2_score+2
                    print("Player 2 won the round.")
                else:
                    p3_score=p3_score+2
                    print("Player 3 won the round.")

            print("Player 1 score is ",p1_score)
            print("Player 2 score is ",p2_score)
            print("Player 3 score is ",p3_score)
            high_score=max(p1_score,p2_score,p3_score)

            if p1_score>p2_score and p1_score>p3_score:
                if p2_score>p3_score:
                    second_high=p2_score
                else:
                    second_high=p3_score
            elif p2_score>p1_score and p2_score>p3_score:
                if p1_score>p3_score:
                    second_high=p1_score
                else:
                    p3_score
            else:
                if p1_score>p2_score:
                    second_high=p1_score
                else:
                    second_high=p2_score
            game_deck.shuffle()

        if no_winner==0:
            if p1_score>p2_score and p1_score>p3_score:
                print("Player 1 won the game with a score of {}. Player 2's score was {} and Player 3's score was {}.".format(p1_score,p2_score,p3_score))
            elif p2_score>p1_score and p2_score>p3_score:
                print("Player 2 won the game with a score of {}. Player 1's score was {} and Player 3's score was {}.".format(p2_score,p1_score,p3_score))
            else:
                print("Player 3 won the game with a score of {}. Player 1's score was {} and Player 2's score was {}.".format(p3_score,p1_score,p2_score))
        else:
            print("Deck ran out before winner could be declared. Player 1's score was {}, Player 2's score was {}, and Player 3's score was {}.".format(p1_score,p2_score,p3_score))
    else:
        p1_score=0
        p2_score=0
        p3_score=0
        p4_score=0
        high_score=0
        second_high=0
        game_deck=deck()
        num_drawn=0
        no_winner=0
        while high_score<21 or high_score-2<second_high:
            if num_drawn==56:
                no_winner=1
                break
            draw_1= input("Player 1 turn: Press d to draw card: ") 
            while draw_1!='d':
                print("Error: Unknown input entered. Please enter d to draw a card: ")
                draw_1=input()
            
            drawn_1=game_deck.draw()
            num_drawn=num_drawn+1
            print("Player 1 drew {}.".format(drawn_1.show_card()))
            if num_drawn==56:
                no_winner=1
                break
            draw_2= input("Player 2 turn: Press d to draw card: ")
            while draw_2!='d':
                print("Error: Unknown input entered. Please enter d to draw a card: ")
                draw_2=input()
            drawn_2=game_deck.draw()
            num_drawn=num_drawn+1
            print("Player 2 drew {}.".format(drawn_2.show_card()))
            if num_drawn==56:
                no_winner=1
                break
            draw_3=input("Player 3 turn: Press d to draw card: ")
            while draw_3!='d':
                print("Error: Unknown input entered. Please enter d to draw a card: ")
                draw_3=input()
            drawn_3=game_deck.draw()
            num_drawn=num_drawn+1
            print("Player 3 drew {}.".format(drawn_3.show_card()))
            if num_drawn==56:
                no_winner=1
                break
            draw_4=input("Player 4 turn: Press d to draw card: ")
            while draw_4!='d':
                print("Error: Unknown input entered. Please enter d to draw a card: ")
                draw_4=input()
            drawn_4=game_deck.draw()
            num_drawn=num_drawn+1
            print("Player 4 drew {}.".format(drawn_4.show_card()))
            if drawn_1.values==15 and drawn_2.values==15 and drawn_3.values==15 and drawn_4.values==15:
                if p1_score-1<0:
                    p1_score=0
                else:
                    p1_score=p1_score-1
                
                if p2_score-1<0:
                    p2_score=0
                else:
                    p2_score=p2_score-1
                
                if p3_score-1<0:
                    p3_score=0
                else:
                    p3_score=p3_score-1

                if p4_score-1<0:
                    p4_score=0
                else:
                    p4_score=p4_score-1
                print("No one won the round (All players drew penalty cards).")
            elif drawn_1.values==15 and drawn_2.values==15 and drawn_3.values==15:
                if p1_score-1<0:
                    p1_score=0
                else:
                    p1_score=p1_score-1
                
                if p2_score-1<0:
                    p2_score=0
                else:
                    p2_score=p2_score-1
                
                if p3_score-1<0:
                    p3_score=0
                else:
                    p3_score=p3_score-1
                p4_score=p4_score+2
                print("Player 4 won the round.")
            elif drawn_1.values==15 and drawn_2.values==15 and drawn_4.values==15:
                if p1_score-1<0:
                    p1_score=0
                else:
                    p1_score=p1_score-1
                
                if p2_score-1<0:
                    p2_score=0
                else:
                    p2_score=p2_score-1
                
                if p4_score-1<0:
                    p4_score=0
                else:
                    p4_score=p4_score-1
                p3_score=p3_score+2
                print("Player 3 won the round.")
            elif drawn_2.values==15 and drawn_3.values==15 and drawn_4.values==15:
                if p3_score-1<0:
                    p3_score=0
                else:
                    p3_score=p3_score-1
                
                if p2_score-1<0:
                    p2_score=0
                else:
                    p2_score=p2_score-1
                
                if p4_score-1<0:
                    p4_score=0
                else:
                    p4_score=p4_score-1
                p1_score=p1_score+2
                print("Player 1 won the round.")
            elif drawn_1.values==15 and drawn_3.values==15 and drawn_4.values==15:
                if p3_score-1<0:
                    p3_score=0
                else:
                    p3_score=p3_score-1
                
                if p1_score-1<0:
                    p1_score=0
                else:
                    p1_score=p1_score-1
                
                if p4_score-1<0:
                    p4_score=0
                else:
                    p4_score=p4_score-1
                p2_score=p2_score+2
                print("Player 2 won the round.")
            elif drawn_1.values==15 and drawn_2.values==15:
                if p1_score-1<0:
                    p1_score=0
                else:
                    p1_score=p1_score-1

                if p2_score-1<0:
                    p2_score=0
                else:
                    p2_score=p2_score-1

                win_card=compare_cards(drawn_4,drawn_3)
                if win_card.values==drawn_4.values and win_card.suits == drawn_4.suits:
                    p4_score=p4_score+2
                    print("Player 4 won the round.")
                else:
                    p3_score=p3_score+2
                    print("Player 3 won the round.")

            elif drawn_1.values==15 and drawn_3.values==15:
                if p1_score-1<0:
                    p1_score=0
                else:
                    p1_score=p1_score-1

                if p3_score-1<0:
                    p3_score=0
                else:
                    p3_score=p3_score-1
                
                win_card=compare_cards(drawn_1,drawn_3)
                if win_card.values==drawn_1.values and win_card.suits == drawn_1.suits:
                    p1_score=p1_score+2
                    print("Player 1 won the round.")
                else:
                    p3_score=p3_score+2
                    print("Player 3 won the round.")
            elif drawn_1.values==15 and drawn_4.values==15:
                if p1_score-1<0:
                    p1_score=0
                else:
                    p1_score=p1_score-1

                if p4_score-1<0:
                    p4_score=0
                else:
                    p4_score=p4_score-1

                win_card=compare_cards(drawn_2,drawn_3)
                if win_card.values==drawn_2.values and win_card.suits == drawn_2.suits:
                    p2_score=p2_score+2
                    print("Player 2 won the round.")
                else:
                    p3_score=p3_score+2
                    print("Player 3 won the round.")
            elif drawn_2.values == 15 and drawn_3.values==15:
                if p2_score-1<0:
                    p2_score=0
                else:
                    p2_score=p2_score-1

                if p3_score-1<0:
                    p3_score=0
                else:
                    p3_score=p3_score-1

                win_card=compare_cards(drawn_1,drawn_4)
                if win_card.values==drawn_1.values and win_card.suits == drawn_1.suits:
                    p1_score=p1_score+2
                    print("Player 1 won the round.")
                else:
                    p4_score=p4_score+2
                    print("Player 4 won the round.")
            elif drawn_2.values ==15 and drawn_4.values==15:
                if p2_score-1<0:
                    p2_score=0
                else:
                    p2_score=p2_score-1
                
                if p4_score-1<0:
                    p4_score=0
                else:
                    p4_score=p4_score-1
                
                win_card=compare_cards(drawn_1,drawn_3)
                if win_card.values==drawn_1.values and win_card.suits == drawn_1.suits:
                    p1_score=p1_score+2
                    print("Player 1 won the round.")
                else:
                    p3_score=p3_score+2
                    print("Player 3 won the round.")
            elif drawn_3.values ==15 and drawn_4.values==15:
                if p3_score-1<0:
                    p3_score=0
                else:
                    p3_score=p3_score-1

                if p4_score-1<0:
                    p4_score=0
                else:
                    p4_score=p4_score-1

                win_card=compare_cards(drawn_2,drawn_1)
                if win_card.values==drawn_1.values and win_card.suits == drawn_1.suits:
                    p1_score=p1_score+2
                    print("Player 1 won the round.")
                else:
                    p2_score=p2_score+2
                    print("Player 2 won the round.")
            elif drawn_1.values==15:
                if p1_score-1<0:
                    p1_score=0
                else:
                    p1_score=p1_score-1

                pos_winner=compare_cards(drawn_2,drawn_3)
                win_card=compare_cards(pos_winner,drawn_4)
                if win_card.values==pos_winner.values and win_card.suits==pos_winner.suits:
                    if pos_winner.values==drawn_2.values and pos_winner.suits==drawn_2.suits:
                        p2_score=p2_score+2
                        print("Player 2 won the round.")
                    else:
                        p3_score=p3_score+2
                        print("Player 3 won the round.")
                else:
                    p4_score=p4_score+2
                    print("Player 4 won the round.")
            elif drawn_2.values==15:
                if p2_score-1<0:
                    p2_score=0
                else:
                    p2_score=p2_score-1

                pos_winner=compare_cards(drawn_1,drawn_3)
                win_card=compare_cards(pos_winner,drawn_4)
                if win_card.values==pos_winner.values and win_card.suits==pos_winner.suits:
                    if pos_winner.values==drawn_1.values and pos_winner.suits==drawn_1.suits:
                        p1_score=p1_score+2
                        print("Player 1 won the round.")
                    else:
                        p3_score=p3_score+2
                        print("Player 3 won the round.")
                else:
                    p4_score=p4_score+2
                    print("Player 4 won the round.")
            elif drawn_3.values==15:
                if p3_score-1<0:
                    p3_score=0
                else:
                    p3_score=p3_score-1


                pos_winner=compare_cards(drawn_1,drawn_2)
                win_card=compare_cards(pos_winner,drawn_4)
                if win_card.values==pos_winner.values and win_card.suits==pos_winner.suits:
                    if pos_winner.values==drawn_2.values and pos_winner.suits==drawn_2.suits:
                        p2_score=p2_score+2
                        print("Player 2 won the round.")
                    else:
                        p1_score=p1_score+2
                        print("Player 1 won the round.")
                else:
                    p4_score=p4_score+2
                    print("Player 4 won the round.")

            elif drawn_4.values == 15:
                if p4_score-1<0:
                    p4_score=0
                else:
                    p4_score=p4_score-1

                pos_winner=compare_cards(drawn_1,drawn_2)
                win_card=compare_cards(pos_winner,drawn_3)
                if win_card.values==pos_winner.values and win_card.suits==pos_winner.suits:
                    if pos_winner.values==drawn_2.values and pos_winner.suits==drawn_2.suits:
                        p2_score=p2_score+2
                        print("Player 2 won the round.")
                    else:
                        p1_score=p1_score+2
                        print("Player 1 won the round.")
                else:
                    p3_score=p3_score+2
                    print("Player 3 won the round.")
            else:
                pos_winner_1=compare_cards(drawn_1,drawn_2)
                pos_winner_2=compare_cards(drawn_3,drawn_4)
                win_card=compare_cards(pos_winner_1,pos_winner_2)

                if win_card.values==pos_winner_1.values and win_card.suits==pos_winner_1.suits:
                    if pos_winner_1.values==drawn_2.values and pos_winner_1.suits==drawn_2.suits:
                        p2_score=p2_score+2
                        print("Player 2 won the round.")
                    else:
                        p1_score=p1_score+2
                        print("Player 1 won the round.")
                else:
                    if pos_winner_2.values == drawn_3.values and pos_winner_2.suits==drawn_3.suits:
                        p3_score=p3_score+2
                        print("Player 3 won the round.")
                    else:
                        p4_score=p4_score+2
                        print("Player 4 won the round.")

                print("Player 1 score is ",p1_score)
                print("Player 2 score is ",p2_score)
                print("Player 3 score is ",p3_score)
                print("Player 4 score is ",p4_score)
                high_score=max(p1_score,p2_score,p3_score,p4_score)
                if p1_score>p2_score and p1_score>p3_score and p1_score>p4_score:
                    if p2_score>p3_score and p2_score>p4_score:
                        second_high=p2_score
                    elif p3_score>p2_score and p3_score>p4_score:
                        second_high=p3_score
                    else:
                        second_high=p4_score
                elif p2_score>p1_score and p2_score>p3_score and p2_score>p4_score:
                    if p1_score>p3_score and p1_score>p4_score:
                        second_high=p1_score
                    elif p3_score>p1_score and p3_score>p4_score:
                        second_high=p3_score
                    else:
                        second_high=p4_score
                elif p3_score>p1_score and p3_score>p2_score and p3_score>p4_score:
                    if p1_score>p2_score and p1_score>p4_score:
                        second_high=p1_score
                    elif p2_score>p1_score and p2_score>p4_score:
                        second_high=p2_score
                    else:
                        second_high=p4_score
                else:
                    if p1_score>p2_score and p1_score>p3_score:
                        second_high=p1_score
                    elif p2_score>p1_score and p2_score>p3_score:
                        second_high=p2_score
                    else:
                        second_high=p3_score
                game_deck.shuffle()

        if no_winner==0:
            if p1_score>p2_score and p1_score>p3_score and p1_score>p4_score:
                print("Player 1 won the game with a score of {}. Player 2's score was {}, Player 3's score was {}, and Player 4's score was {}.".format(p1_score,p2_score,p3_score,p4_score))
            elif p2_score>p1_score and p2_score>p3_score and p2_score>p4_score:
                print("Player 2 won the game with a score of {}. Player 1's score was {}, Player 3's score was {}, and Player 4's score was {}.".format(p2_score,p1_score,p3_score,p4_score))
            elif p3_score>p1_score and p3_score>p2_score and p3_score>p4_score:
                print("Player 3 won the game with a score of {}. Player 1's score was {}, Player 2's score was {}, and Player 4's score was {}.".format(p3_score,p1_score,p2_score,p4_score))
            else:
                print("Player 4 won the game with a score of {}. Player 1's score was {}, Player 2's score was {}, and Player 3's score was {}.".format(p4_score,p1_score,p2_score,p3_score))
        else:
            print("Deck ran out before winner could be declared. Player 1's score was {}, Player 2's score was {}, Player 3's score was {}, and Player 4's score was {}.".format(p1_score,p2_score,p3_score,p4_score))