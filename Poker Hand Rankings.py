#Card type suit
card_typesuit = ['s', 'h', 'd', 'c']
#Card type point
card_typepoint = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

#Input Card
cards = []

c = 0
while c < 5:
    card = input("Enter a Boardcard: ")
    if card[:1] in card_typesuit and card[2:] in card_typepoint:
        if card not in cards:
            cards.append(card)
            c += 1
        else:
            print("This card has already. Try again.")
    else:
        print("This card does not exist. Try again.")

print("------------------------------")

c = 0
while c < 2:
    card = input("Enter a Player's Card: ")
    if card[:1] in card_typesuit and card[2:] in card_typepoint:
        if card not in cards:
            cards.append(card)
            c += 1
        else:
            print("This card has already. Try again.")
    else:
        print("This card does not exist. Try again.")

print("------------------------------")

#Card suit
suit = []
for c in cards:
    suit.append(c[:1])
    
#Card point
point = []
for c in cards:
    point.append(c[2:])

#Find same suit 5 card
s_suit = suit.count('s')
h_suit = suit.count('h')
d_suit = suit.count('d')
c_suit = suit.count('c')
if s_suit >= 5:
    real_suit = 's'
elif h_suit >= 5:
    real_suit = 'h'
elif d_suit >= 5:
    real_suit = 'd'
elif c_suit >= 5:
    real_suit = 'c'
else:
    real_suit = 'none'

#special card
special_card = ['A', 'J', 'Q', 'K']
special_card_point = [1, 11, 12, 13, 14]

#if <find_answer = True> Program will check condition.
find_answer = True

#Royal Straight Flush
if find_answer:
    royal = ['A', 'K', 'Q', 'J', '10']
    now_royal = []
    index = 0
    while index < 7:
        if suit[index] == real_suit:
            if point[index] in royal and point[index] not in now_royal:
                now_royal.append(point[index])
        index += 1
    if len(now_royal) == 5:
        print("Royal Straight Flush")
        find_answer = False

#Straight Flush
if find_answer:
    now_straight_flush = []
    index = 0
    while index < 7:
        if suit[index] == real_suit:
            if point[index] == special_card[0]:
                now_straight_flush.append(special_card_point[0])
            elif point[index] == special_card[1]:
                now_straight_flush.append(special_card_point[1])
            elif point[index] == special_card[2]:
                now_straight_flush.append(special_card_point[2])
            elif point[index] == special_card[3]:
                now_straight_flush.append(special_card_point[3])
            else:
                now_straight_flush.append(int(point[index]))
        index += 1
    if len(now_straight_flush) >= 5:
        now_straight_flush.sort()
        if len(now_straight_flush) == 5:
            if now_straight_flush[0] == now_straight_flush[1]-1 == now_straight_flush[2]-2 == now_straight_flush[3]-3 == now_straight_flush[4]-4:
                print("Straight Flush")
                find_answer = False
        elif len(now_straight_flush) == 6:
            if now_straight_flush[0] == now_straight_flush[1]-1 == now_straight_flush[2]-2 == now_straight_flush[3]-3 == now_straight_flush[4]-4:
                print("Straight Flush")
                find_answer = False
            elif now_straight_flush[1] == now_straight_flush[2]-1 == now_straight_flush[3]-2 == now_straight_flush[4]-3 == now_straight_flush[5]-4:
                print("Straight Flush")
                find_answer = False
        elif len(now_straight_flush) == 7:
            if now_straight_flush[0] == now_straight_flush[1]-1 == now_straight_flush[2]-2 == now_straight_flush[3]-3 == now_straight_flush[4]-4:
                print("Straight Flush")
                find_answer = False
            elif now_straight_flush[1] == now_straight_flush[2]-1 == now_straight_flush[3]-2 == now_straight_flush[4]-3 == now_straight_flush[5]-4:
                print("Straight Flush")
                find_answer = False
            elif now_straight_flush[2] == now_straight_flush[3]-1 == now_straight_flush[4]-2 == now_straight_flush[5]-3 == now_straight_flush[6]-4:
                print("Straight Flush")
                find_answer = False
        
#Four of a Kind
if find_answer:
    for typepoint in card_typepoint:
        if point.count(typepoint) == 4:
            print("Four of a Kind")
            find_answer = False

#Full House
if find_answer:
    three = 0
    two = 0
    for typepoint in card_typepoint:
        if point.count(typepoint) == 3:
            three += 1
        elif point.count(typepoint) == 2 and two == 0:
            two += 1
    if three == 1 and two == 1:
        print("Full House")
        find_answer = False
    elif three == 2:
        print("Full House") 
        find_answer = False

#Flush
if find_answer:
    for typesuit in card_typesuit:
        if suit.count(typesuit) >= 5:
            print("Flush")   
            find_answer = False

#Straight
ace_check = 0 
while find_answer and ace_check < 2:
    now_straight_all = []
    now_straight = []
    index = 0
    while index < 7:
        if point[index] == special_card[0]:
            if ace_check == 0: #Straight <Ace-Low>
                now_straight_all.append(special_card_point[0]) 
            elif ace_check == 1: #Straight <Ace-High>
                now_straight_all.append(special_card_point[4]) 
        elif point[index] == special_card[1]:
            now_straight_all.append(special_card_point[1])
        elif point[index] == special_card[2]:
            now_straight_all.append(special_card_point[2])
        elif point[index] == special_card[3]:
            now_straight_all.append(special_card_point[3])
        else:
            now_straight_all.append(int(point[index]))
        index += 1
    
    for check in now_straight_all:
        if check not in now_straight:
            now_straight.append(check)
        else:
            now_straight.append(-1)         
    now_straight.sort()
    
    if now_straight[0] == now_straight[1]-1 == now_straight[2]-2 == now_straight[3]-3 == now_straight[4]-4:
        print("Straight")
        find_answer = False
    elif now_straight[1] == now_straight[2]-1 == now_straight[3]-2 == now_straight[4]-3 == now_straight[5]-4:
        print("Straight")
        find_answer = False
    elif now_straight[2] == now_straight[3]-1 == now_straight[4]-2 == now_straight[5]-3 == now_straight[6]-4:
        print("Straight")
        find_answer = False
    ace_check += 1

#Three of a Kind
if find_answer:
    three = 0
    for typepoint in card_typepoint:
        if point.count(typepoint) == 3:
            three += 1
    if three >= 1:
        print("Three of a Kind")
        find_answer = False

#Two Pair
if find_answer:
    two = 0
    for typepoint in card_typepoint:
        if point.count(typepoint) == 2:
            two += 1
    if two >= 2:
        print("Two Pair")
        find_answer = False

#One Pair
if find_answer:
    two = 0
    for typepoint in card_typepoint:
        if point.count(typepoint) == 2:
            two += 1
    if two == 1:
        print("One Pair")
        find_answer = False

#High Card
if find_answer:
    print("High Card")