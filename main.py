from random import shuffle
from itertools import product

J = 10
Q = 10
K = 10
A = 11
player_sum = 0
dealer_sum = 0

cards = (2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A)
suits = ('hearts', 'diamonds', 'spades', 'clubs')
deck = list(product(cards, suits))

shuffle(deck)

#print statements for player cards
def Player_Card_1():
  print(player_hand[0], "of", player_hand[1])
def Player_Card_2():
  print(player_hand[2], "of", player_hand[3])
def Player_Card_3():
  print(player_hand[4], "of", player_hand[5])
def Player_Card_4():
  print(player_hand[6], "of", player_hand[7]) 
def Player_Card_5():
  print(player_hand[8], "of", player_hand[9]) 

#print statements for dealer's cards
def Dealer_Card_1():
  print(dealer_hand[0],"of",dealer_hand[1])
def Dealer_Card_2():
  print(dealer_hand[2],"of",dealer_hand[3])
def Dealer_Card_3():
  print(dealer_hand[4],'of',dealer_hand[5])
def Dealer_Card_4():
  print(dealer_hand[6],'of',dealer_hand[7])
def Dealer_Card_5():
  print(dealer_hand[8],'of',dealer_hand[9])










print("Welcome to Blackjack")

print("Dealing cards...")

while len(deck) > 0:
  #player Helpers
    def BJ_check():  
      if player_sum == 21:
          print("Blackjack!")
    def print_player_sum():
      print(f"Player's Current Sum: {player_sum}")
      print("\n")
  #dealer Helpers
    def dealer_BJ_check():
      if dealer_sum == 21:
          print("Dealer has Blackjack")
    def dealer_above16_check():  
      if dealer_sum > 16 and dealer_sum < 21:
        print("\n")
        print("Dealer is above 16. They stay")
    def print_dealer_sum():
      print(f"Dealer's Current Sum: {dealer_sum}")
      print("\n")      
  #comparison Helper
    def BJ_Standoff():  
      if player_sum == 21 and dealer_sum != 21:
        print("Blackjack!")
      if player_sum == 21 and dealer_sum == 21:
        print("Tie for Blackjack. Dealer Wins")
      if player_sum != 21 and dealer_sum == 21:
        print("Dealer has Blackjack.")
    
    
    
  #deal player initial 2 cards
    print("\n")
    player_hand = deck.pop() + deck.pop()
    player_sum = player_hand[0] + player_hand[2]
    print("Your Hand:")
    Player_Card_1()
    Player_Card_2()
    print_player_sum()
    
    
    #deal dealer initial 2 cards
    dealer_hand = deck.pop() + deck.pop()
    dealer_sum = dealer_hand[0] + dealer_hand[2]
    print("\n")
    print("Dealer's Hand:")
    Dealer_Card_1()
    Dealer_Card_2()
    print_dealer_sum()

    #Check for 2 card blackjack
    BJ_Standoff()

    
    #first input
    print("\n")
    first = input("Hit or Stay? ")
    
    #first player hit scenario
    if first == "Hit":
        print("\n")
        player_hand += deck.pop()
        print("Your Hand:")
        Player_Card_1()
        Player_Card_2()
        Player_Card_3()
        player_sum += player_hand[4]
        if player_sum > 21 and A in player_hand:
          player_sum -= 11
          player_sum += 1
        print_player_sum()
        BJ_check()
        if player_sum > 21:
          print("\n")
          print("Busted! Dealer wins")
          continue
        
    #first player stay scenario      
    if first == "Stay":
      pass
    
    #first dealer decision
    #store whether dealer was above or below 16 before 1st decision
    dealer_cont_1 = dealer_sum
    dealer_first = ""
    #check if dealer is at 16
    if dealer_sum == 16:
      print("\n")
      print("Dealer is at 16. They stay")
      dealer_first = "Stay"
    #check is dealer is above 16 but not busted
    elif dealer_sum > 16 and dealer_sum < 21:
      print("\n")
      print("Dealer is above 16. They stay")
    #check is dealer is below 16, in which case they hit
    elif dealer_sum < 16:
      print("Dealer under 16. Dealer takes the hit")
      dealer_hand += deck.pop()
      dealer_sum += dealer_hand[4]
      print("\n")
      print("Dealer's Hand:")
      Dealer_Card_1()
      Dealer_Card_2()
      Dealer_Card_3()
      if dealer_sum > 21 and A in player_hand:
          dealer_sum -= 11
          dealer_sum += 1
    print_dealer_sum()
    #check if dealer busted on first hit
    if dealer_sum > 21:
          print("\n")
          print("Dealer busted. You win!")
          continue
    
    
    if first != "Stay" and player_sum != 21:
      second = input("Hit or Stay? ")
      if second == "Hit":
        print("\n")
        player_hand += deck.pop()
        Player_Card_1()
        Player_Card_2()
        Player_Card_3()
        Player_Card_4()
        player_sum += player_hand[6]
        print(f"Current Sum: {player_sum}")
        print("\n")
        if player_sum > 21 and player_hand[5] == A:
          player_sum -= 11
          player_sum += 1
      BJ_check()
      if player_sum > 21:
        print("\n")
        print("Busted! Dealer wins")
        continue
      if second == "Stay":
        pass

    
    #check 2nd time if dealer was under 16
    if dealer_sum == 16:
      print("\n")
      print("Dealer is at 16. They stay")
    if dealer_sum < 16:
      print("\n")
      print("Dealer under 16. Dealer takes the hit")
      dealer_hand += deck.pop()
      dealer_sum += dealer_hand[6]
      print("\n")
      print("Dealer's Hand:")
      Dealer_Card_1()
      Dealer_Card_2()
      Dealer_Card_3()
      Dealer_Card_4()
    if dealer_first != "Stay":
      print_dealer_sum()
    if dealer_sum > 21:
      print("\n")
      print("Dealer busted. You win!")
      continue
    if dealer_cont_1 < 16:
      dealer_above16_check()
    dealer_cont_2 = dealer_sum


    if dealer_sum < 16:
      print("\n")
      print("Dealer under 16. Dealer takes the hit")
      dealer_hand += deck.pop()
      dealer_sum += dealer_hand[8]
      
      print("\n")
      print("Dealer's Hand:")
      Dealer_Card_1()
      Dealer_Card_2()
      Dealer_Card_3()
      Dealer_Card_4()
      Dealer_Card_5()
   
    if dealer_sum > 21:
        print("\n")
        print("Dealer busted. You win!")
        continue
    
  
    if dealer_cont_2 < 16:
      dealer_above16_check()
    if player_sum > dealer_sum:
      print("\n")
      print(f"{player_sum} beats {dealer_sum}. You win!")
    elif player_sum < dealer_sum:
      print("\n")
      print(f"{dealer_sum} beats {player_sum}. Dealer wins")
    else:
      print("\n")
      print(f"Tie at {player_sum}. Dealer wins")
    
    





print("Run again to reshuffle deck")
