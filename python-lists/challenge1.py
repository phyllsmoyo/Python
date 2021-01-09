### Create a list for a standard deck of cards ###

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
deck = []

for suit in suits:
    for number in numbers:
        deck.append(f"{number} of {suit}")

print(f"There are {len(deck)} cards in the deck")

### Step 3 - Randomly choose five cards to add to a player's hand ###

print("Dealing...")

import random

player1 = random.choices(deck, k=5)
print(f"{len(player1)} cards delt to Player1 are: {player1}")

# Remove the chosen cards from the deck
for card in player1:
    if card in deck:
        deck.remove(card)

print(f"Cards remaining in the deck are {len(deck)}")

print(len(deck))
