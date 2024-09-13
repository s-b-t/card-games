import secrets

# Define the ranks and suits
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['♥︎', '♠︎', '♦︎', '♣︎']

# Create the deck of cards as a list of (rank + suit) tuples
deck = [(rank + suit) for rank in ranks for suit in suits]

# Shuffle the deck using the CSRNG (cryptographically secure random number generator)
secrets.SystemRandom().shuffle(deck)

def displayCards(cards):
    # Displays all the cards in the cards list
    rows = ['', '', '', '', '']

    for card in cards:
        # Prints top line of card
        rows[0] += ' ___  '
        
        # Prints the card's front
        rank, suit = card[:-2], card[-2:]
        rows[1] += '|{} | '.format(rank.ljust(2))
        rows[2] += '| {} | '.format(suit)
        rows[3] += '|_{}| '.format(rank.rjust(2, '_'))
            
    # Prints each row on the screen
    for row in rows:
        print(row)

def dealHand():
    return [deck.pop(0) for _ in range(2)]

def burnCard():
    return deck.pop(0)

def dealFlop():
    burnCard()
    return [deck.pop(0) for _ in range(3)]

def dealTurn():
    burnCard()
    return deck.pop(0)

def dealRiver():
    burnCard()
    return deck.pop(0)

def getPlayerDecision():
    while True:
        decision = input("Do you want to (B)et, (C)heck, or (F)old? (B/C/F): ").strip().upper()
        print()
        if decision in ['B', 'C', 'F']:
            return decision
        print("Invalid choice. Please enter 'B' for Bet, 'C' for Check, or 'F' for Fold.")
        print()

def main():
    # Deal initial hand
    hand = dealHand()
    print("YOUR HAND:")
    displayCards(hand)
    
    while True:
        decision = getPlayerDecision()
        
        if decision == 'F':
            print("You folded. Round over.")
            break
        elif decision == 'B':
            print("You chose to Bet.\n")
            input("How much would you like to bet? ")
            # You can add more betting logic here if needed
        elif decision == 'C':
            print("You Checked.")
            # Proceed with the game

        # Deal and display the flop, turn, and river
        print("\nTHE FLOP:")
        flop = dealFlop()
        displayCards(flop)

        print("\nTHE TURN:")
        turn = dealTurn()
        displayCards([turn])

        print("\nTHE RIVER:")
        river = dealRiver()
        displayCards([river])
        
        # End the game loop after showing all cards
        print("The game is now over.")
        break

if __name__ == "__main__":
    main()