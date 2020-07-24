
from random import shuffle
from itertools import product

J = 10
Q = 10
K = 10
A = 11
player_sum = 0
dealer_sum = 0




cards = (2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A)
suits = ('hearts','diamonds','spades','clubs')
deck = list(product(cards,suits))

shuffle(deck)


print ("Welcome to Blackjack Bitch")


print("Dealing cards...")

while len(deck) > 0:
 #deal player initial 2 cards
  player_hand = deck.pop() + deck.pop()
  player_sum = player_hand[0] + player_hand[2]
  print (player_hand[0],"of",player_hand[1])
  print (player_hand[2],"of",player_hand[3])
  print (f"Current Sum: {player_sum}")
  first = input("Hit or Stay? ")
  if first == "Hit":
    player_hand += deck.pop()
    print(player_hand)
  if first == "Stay":
    continue
  


print("Deck is Up!")