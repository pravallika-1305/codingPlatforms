cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
import random
def special_card_generation(point_card,card_list):
    for i in range(len(card_list)):
        if point_card == card_list[i] and point_card in "QK":
            return card_list[i + 1]
        else :
            return card_list[i]





n = (input())
cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

value_dict = {'2' : 2,'3' : 3,'4' : 4,'5' : 5,'6' : 6,'7' : 7,'8' : 8,'9' : 9,'T' : 10,'J' : 11,'Q' : 12,'K' : 13,'A' : 14}
point_card = random.choice(cards)
choice = 'Q'
if choice is n :
    print(special_card_generation(choice,cards))
#print(point_card)



