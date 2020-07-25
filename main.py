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

#print statements for dealer's cards
def Dealer_Card_1():
  print(dealer_hand[0],"of",dealer_hand[1])
def Dealer_Card_2():
  print(dealer_hand[2],"of",dealer_hand[3])
def Dealer_Card_3():
  print(dealer_hand[4],'of',dealer_hand[5])


   


print("Welcome to Blackjack Bitch")

print("Dealing cards...")

while len(deck) > 0:
    #deal player initial 2 cards
    print("\n")
    player_hand = deck.pop() + deck.pop()
    player_sum = player_hand[0] + player_hand[2]
    print("Your Hand:")
    Player_Card_1()
    Player_Card_2()
    print(f"Current Sum: {player_sum}")
    
    
    #deal dealer initial 2 cards
    dealer_hand = deck.pop() + deck.pop()
    dealer_sum = dealer_hand[0] + dealer_hand[2]
    print("\n")
    print("Dealer's Hand:")
    Dealer_Card_1()
    Dealer_Card_2()
    print(f"Current Sum: {dealer_sum}")

    if player_sum == 21 and dealer_sum != 21:
      print("Blackjack!")
      pass
    if player_sum == 21 and dealer_sum == 21:
     print("Tie for Blackjack. Dealer Wins")
     pass
    if player_sum != 21 and dealer_sum == 21:
      print("Dealer has Blackjack. Dealer Wins")
      pass

    
    print("\n")
    first = input("Hit or Stay? ")
    if first == "Hit":
        print("\n")
        player_hand += deck.pop()
        Player_Card_1()
        Player_Card_2()
        Player_Card_3()
        player_sum += player_hand[4]
        print(f"Current Sum: {player_sum}")
        if player_sum == 21:
          print("Blackjack!")
          pass
        if player_sum > 21:
          print("Busted! Dealer wins")
          pass
    if first == "Stay":
        continue
    if dealer_sum <= 16:
      print("Dealer under 16. Dealer takes the hit")
      dealer_hand += deck.pop()


print("Run again to reshuffle deck")
