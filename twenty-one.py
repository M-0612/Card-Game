"""
Card game based on the game twenty-one;
For rules, see readme.md
"""

import random
import sys
import time
from typing import Tuple, Dict, List

# Initialize set of 32 cards
def initialize_card_set() -> Dict[str, int]:
    point_dict = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
    suits = ['of Clubs', 'of Spades', 'of Hearts', 'of Diamonds']

    # Iterate over point dict, combining each key with each suit and store as key:value pair in card set
    return {f"{card} {suit}": point for card, point in point_dict.items() for suit in suits}

# Initalize players
def initialize_players(max_players: int) -> List[str]:
    # Ask player to confirm game start
    while True:
        play = input("Would you like to start the game? (y/n): ").lower()
        if play in ['y', 'n']:
            if play == 'n':
                print("End game.")
                sys.exit()
            break
        else:
            print("Input invalid. Please try again.")

    # Ask for number of players
    while True:
        try:
            # Check, if input is a number
            player_number = int(input("Number of players (1-4): "))

            # Check, if the number is in the stipulated range
            if 1 <= player_number <= max_players:
                break
            else:
                print(f"Please enter a number from 1 to 4.")

        # If input is not a number, go back
        except ValueError:
            print(f"Invalid input. Please enter a number.")

    # Initialize list of players, to store names
    return [input(f"Name of player {i + 1}: ") for i in range(player_number)]


# Draw a random card from the card set
def draw_card(card_set: Dict[str, int]) -> Tuple[str, int]:
    card_name, card_score = random.choice(list(card_set.items()))
    # Remove card from the card set and return its value
    return card_name, card_set.pop(card_name)

# Add drawn card to cards of players/ dealer
def update_cards(cards_dict: Dict[str, int], card_name: str, card_score: int):
    cards_dict[card_name] = card_score

# Calculate points of player or dealer
def calculate_score(cards_dict: Dict[str, int]) -> int:
    total_score = sum(cards_dict.values())
    # Adjust for Aces if total score exceeds 21 (reduce 10 points per Ace)
    ace_count = sum(1 for card in cards_dict if 'Ace' in card)
    while total_score > 21 and ace_count:
        total_score -= 10
        ace_count -= 1
    return total_score

# Determine and declare winner
def declare_winner(player_scores: Dict[str, int], dealer_score: int):
    players_with_21 = [name for name, score in player_scores.items() if score == 21]
    if dealer_score == 21:
        if players_with_21:
            print(f"Tie! Both the bank and player(s) {', '.join(players_with_21)} have 21 points.\n")
        else:
            print(f"The dealer wins with 21 points!\n")
    elif players_with_21:
        print(f"The winner(s): {', '.join(players_with_21)} with 21 points!")
    elif all(score > 21 for score in player_scores.values()):
        print(f"All players have lost. The dealer wins.\n")
    else:
        closest_score = max(score for score in player_scores.values() if score < 21)
        winners = [name for name, score in player_scores.items() if score == closest_score]
        if dealer_score <= 21 and dealer_score >= closest_score:
            print(f"The dealer wins with {dealer_score} points!")
        else:
            print(f"The winner(s): {', '.join(winners)} with {closest_score} points!")

def main():
    max_players = 4
    card_set = initialize_card_set()
    players = initialize_players(max_players)
    player_cards = {player: {} for player in players}
    dealer_cards = {}

    print(f"\nFirst Round: Start\n")

    # Players receive first card each
    for player in players:
        card_name, card_score = draw_card(card_set)
        print(f"{player} receives {card_name}.")
        update_cards(player_cards[player], card_name, card_score)
        current_score = calculate_score(player_cards[player])
        print(f"{player}'s score is now {current_score}.\n")

    # Dealer receives first card
    card_name, card_score = draw_card(card_set)
    print(f"The dealer draws {card_name}.")
    update_cards(dealer_cards, card_name, card_score)
    dealer_score = calculate_score(dealer_cards)
    print(f"The dealer's score is now {dealer_score}.\n")

    print("Second Round: Start\n")

    # Players receive second card each
    for player in players:
        while True:
            card_name, card_score = draw_card(card_set)
            print(f"{player} draws {card_name}.")
            update_cards(player_cards[player], card_name, card_score)
            current_score = calculate_score(player_cards[player])
            print(f"{player}'s score is now {current_score}.\n")
            if current_score > 21:
                print(f"{player}'s score passed 21. {player} lost.\n")
                break
            elif current_score == 21:
                break
            # Players are asked if they want further cards
            choice = input(f"{player}, do you want another card? (y/n): ").lower()
            if choice == 'n':
                print()
                break
            time.sleep(0.5)

    print("It's the dealer's turn.\n")

    # Dealer round
    while True:
        card_name, card_score = draw_card(card_set)
        print(f"The dealer draws {card_name}.")
        update_cards(dealer_cards, card_name, card_score)
        dealer_score = calculate_score(dealer_cards)
        print(f"The dealer's score is now {dealer_score}.\n")
        if dealer_score >= 17:
            break
        time.sleep(0.5)

    # Determine and declare the winner
    player_scores = {player: calculate_score(cards) for player, cards in player_cards.items()}
    declare_winner(player_scores, dealer_score)

if __name__ == "__main__":
    main()
