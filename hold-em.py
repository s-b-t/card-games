import secrets

# Define the ranks and suits
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = [' ♥︎', ' ♠︎', ' ♦︎', ' ♣︎']

# Create the deck of cards as a list of (rank, suit) tuples
deck = [(rank + suit) for rank in ranks for suit in suits]

# Shuffle the deck using the CSRNG (cryptographically secure random number generator)
secrets.SystemRandom().shuffle(deck)

# Function to deal cards (i.e. 2 cards)
def dealHand():
    return [deck.pop(0) for _ in range(2)]

def burnCard():
    # Burn the top card from the deck (the first element of the list)
    return deck.pop(0)

def dealFlop():
    # Burn the top card and deal the next 3 cards in the list (Flop cards)
    burnCard()
    return [deck.pop(0) for _ in range(3)]

def dealTurn():
    # Burn the top card and deal the next card in the list (Turn card)
    burnCard()
    return deck.pop(0)

def dealRiver():
    # Burn the top card and deal the next card in the list (River card)
    burnCard()
    return deck.pop(0)

# Example: Deal a 2-card hand, the Flop (3 cards), the Turn (1 card), and the River (1 card)
hand = dealHand()
flop = dealFlop()
turn = dealTurn()
river = dealRiver()

print()
print("Hand:", hand)
print()
print("Flop:", flop)
print("Turn:", turn)
print("River:", river)
print()



