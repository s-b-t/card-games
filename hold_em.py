import secrets
import sys

# Define the ranks and suits
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['♥︎', '♠︎', '♦︎', '♣︎']
money = 5000

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

def getPlayerDecision(hand, canBet):
    print("YOUR HAND:")
    displayCards(hand)
    while True:
        if canBet:
            decision = input("Do you want to (B)et, (C)heck, (F)old, or go (A)ll in? (B/C/F/A): ").strip().upper()
        else:
            decision = input("Do you want to (C)heck, (F)old, or go (A)ll in? (C/F/A): ").strip().upper()
        
        print()
        if decision in ['B', 'C', 'F', 'A'] and (canBet or decision != 'B'):
            return decision
        print("Invalid choice. Please enter 'B' for Bet, 'C' for Check, 'F' for Fold, or 'A' for All in.")
        print()

def getBet(maxBet):
    while True:
        bet = input("How much would you like to bet? ($1 - ${}, or QUIT) ".format(maxBet))
        if bet == "QUIT":
            print("Sore loser! Better luck next time!")
            sys.exit()

        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet

def main():
    global money
    
    while True:
        # Reset deck and shuffle for a new round
        deck = [(rank + suit) for rank in ranks for suit in suits]
        secrets.SystemRandom().shuffle(deck)
        
        # Deal initial hand
        hand = dealHand()
        
        # Keep track of community cards (flop, turn, river)
        communityCards = []

        # Track stages (flop, turn, river)
        stagesRevealed = {
            "flop": False,
            "turn": False,
            "river": False
        }

        while True:
            print("\nPiggy Bank:", "$", money)
            
            if money <= 0:
                print("You poor bastard! Good thing you weren't gambling with your life savings!")
                print("Better luck next time!")
                sys.exit()
            
            # Determine if the player can bet (i.e., before the river)
            canBet = not stagesRevealed["river"]
            
            # Get player's decision (Bet, Check, Fold, All in)
            decision = getPlayerDecision(hand, canBet)
            
            if decision == 'F':
                print("You folded. Round over.")
                break
            elif decision == 'B':
                print("You chose to Bet.\n")
                bet = getBet(money)
                money -= bet
                print(f"You bet ${bet}. Remaining money: ${money}\n")
            elif decision == 'C':
                print("You Checked.")
            elif decision == 'A':
                print("You went All in!")
                money = 0  # Player's entire money is depleted
                
                # Reveal all remaining community cards
                if not stagesRevealed["flop"]:
                    print("\nTHE FLOP:")
                    flop = dealFlop()
                    communityCards.extend(flop)
                    stagesRevealed["flop"] = True
                    displayCards(communityCards)
                    input("Press Enter to see the Turn card...")
                if not stagesRevealed["turn"]:
                    print("\nTHE TURN:")
                    turn = dealTurn()
                    communityCards.append(turn)
                    stagesRevealed["turn"] = True
                    displayCards(communityCards)
                    input("Press Enter to see the River card...")
                if not stagesRevealed["river"]:
                    print("\nTHE RIVER:")
                    river = dealRiver()
                    communityCards.append(river)
                    stagesRevealed["river"] = True
                    displayCards(communityCards)
                
                # End the round after all cards are revealed
                print("\nRound over. Press Enter to start a new round or type 'QUIT' to exit.")
                if input().strip().upper() == "QUIT":
                    print("Thanks for playing! See you next time.")
                    sys.exit()
                else:
                    break  # Start a new round

            # Reveal community cards progressively, appending new cards
            if not stagesRevealed["flop"]:
                print("\nTHE FLOP:")
                flop = dealFlop()
                communityCards.extend(flop)
                stagesRevealed["flop"] = True
            elif not stagesRevealed["turn"]:
                print("\nTHE TURN:")
                turn = dealTurn()
                communityCards.append(turn)
                stagesRevealed["turn"] = True
            elif not stagesRevealed["river"]:
                print("\nTHE RIVER:")
                river = dealRiver()
                communityCards.append(river)
                stagesRevealed["river"] = True
            
            # Display all community cards together
            print("\nCommunity Cards:")
            displayCards(communityCards)
            
            # Last chance to Bet, Check, or Fold after the river card is revealed
            if stagesRevealed["river"]:
                decision = getPlayerDecision(hand, False)
                
                if decision == 'F':
                    print("You folded. Round over.")
                elif decision == 'B':
                    print("You chose to Bet.\n")
                    bet = getBet(money)
                    money -= bet
                    print(f"You bet ${bet}. Remaining money: ${money}\n")
                elif decision == 'C':
                    print("You Checked.")
                elif decision == 'A':
                    print("You went All in!")
                    money = 0  # Player's entire money is depleted
                    print("\nAll 5 community cards:")
                    displayCards(communityCards)
                
                # End the round after the player's final decision
                print("\nRound over. Press Enter to start a new round or type 'QUIT' to exit.")
                if input().strip().upper() == "QUIT":
                    print("Thanks for playing! See you next time.")
                    sys.exit()
                else:
                    break  # Start a new round

if __name__ == "__main__":
    main()