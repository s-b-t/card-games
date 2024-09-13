import secrets

# Define the ranks and suits
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['♥︎', '♠︎', '♦︎', '♣︎']

# Create the deck of cards as a list of (rank + suit) tuples
deck = [(rank + suit) for rank in ranks for suit in suits]

# Shuffle the deck using the CSRNG (cryptographically secure random number generator)
secrets.SystemRandom().shuffle(deck)

def displayCards(cards):
    # Displays all the cards in the cards list (text displayed on each row).
    rows = ['', '', '', '', '']

    for card in cards:
        # Prints top line of card:
        rows[0] += ' ___  '
        
        # Prints the card's front:
        rank, suit = card[:-2], card[-2:]
        rows[1] += '|{} | '.format(rank.ljust(2))
        rows[2] += '| {} | '.format(suit)
        rows[3] += '|_{}| '.format(rank.rjust(2, '_'))
            
    # Prints each row on the screen:
    for row in rows:
        print(row)

# Function to deal a hand (i.e. 2 cards)
def dealHand():
    return [deck.pop(0) for _ in range(2)]

def burnCard():
    # Burn the top card from the deck (the first element of the list)
    return deck.pop(0)

def dealFlop():
    # Burn the top card and deal the next 3 cards in the deck (Flop cards)
    burnCard()
    return [deck.pop(0) for _ in range(3)]

def dealTurn():
    # Burn the top card and deal the next card in the deck (Turn card)
    burnCard()
    return deck.pop(0)

def dealRiver():
    # Burn the top card and deal the next card in the deck (River card)
    burnCard()
    return deck.pop(0)

# Example: Deal a hand (2 cards), the Flop (3 cards), the Turn (1 card), and the River (1 card)
hand = dealHand()
flop = dealFlop()
turn = dealTurn()
river = dealRiver()

# Display the cards
print("Your Hand:")
displayCards(hand)

print("\nFlop:")
displayCards(flop)

print("\nTurn:")
displayCards([turn])

print("\nRiver:")
displayCards([river])