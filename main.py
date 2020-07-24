from random import shuffle
from itertools import product
cards = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
suits = ('hearts','diamonds','spades','clubs')
deck = list(product(cards,suits))

shuffle(deck)


print ("Welcome to Blackjack Bitch")


print("Dealing cards...")

while len(deck) > 0:
 #deal player initial 2 cards
  player_hand = deck.pop() + deck.pop()
  print (player_hand)
  first = input("Hit or Stay? ")
  if first == "Hit":
    player_hand += deck.pop()
    print(player_hand)


print("Deck is Up!")