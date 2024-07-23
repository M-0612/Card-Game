"""
Card game based on the game twenty-one;
For rules, see readme.md
"""

import random
import sys
import time
from typing import Tuple

# Initialize set of 32 cards
def initialize_card_set() -> dict:

    card_set = {}
    point_dict = {7: 7, 8: 8, 9: 9, 10: 10, 'Jack': 2, 'Queen': 3, 'King': 4, 'Ace': 11}
    suits = ['of Clubs', 'of Spades', 'of Hearts', 'of Diamonds']

    # Iterate over point dict, combining each key with each suit and store in card set
    for card, point in point_dict.items():
        for suit in suits:
            # Construct card by concatenating point and suit
            new_card = f"{card} {suit}"
            # Add card to card set
            card_set[new_card] = point

    return card_set

# Initalize players
def initialize_players(max_players: int) -> list:
    # Ask player to confirm game start
    while True:
        play = input("Would you like to start the game? (y/n): ").lower()
        if (play == 'n'):
            print("End game.")
            quit()
        elif (play == 'y'):
            break
        else:
            print("Input invalid. Please try again.")

    # Ask for number of players
    while True:
        try:
            # Check, if input is a number
            player_number = int(input("Number of players (1-4): "))

            # Check, if the number is in the stipulated range
            if not (0 < player_number < (max_players + 1)):
                print(f"Please enter a number from 1 to 4.")
                continue
            else:
                break

        # If input is not a number, go back
        except ValueError:
            print(f"Invalid input. Please enter a number.")
            continue

    # Initialize list of players, to store names
    player_names = [input(f"Name of player {i + 1}: ") for i in range(player_number)]

    return player_names


# Draw a random card from the card set
def draw_card(card_set) -> Tuple[str, int]:

    card_name, card_score = random.choice(list(card_set.items()))
    # Remove card from the card set
    del card_set[card_name]
    return card_name, card_score

# Add drawn card to cards of given player in player cards dict list
def update_player_cards(player_cards_list, player, card_name, card_score) -> None:

    # Iterate through dictionaries per player in list
    for score_dict in player_cards_list:
        # In the dict with the name of the player
        if player in score_dict:
            # Check, if the value of the key is a dictionary
            if isinstance(score_dict[player], dict):
                # If so, in the dict of the player, enter new card and score
                score_dict[player][card_name] = card_score
            else:
                # If not, convert current value in dict and add card name and score
                score_dict[player] = {card_name: card_score}
            # Stop looking in other dictionaries
            break

# Add drawn card to bank cards dict
def update_bank_cards(bank_cards_dict, card_name, card_score) -> None:

    bank_cards_dict[card_name] = card_score

# Calculate current score of player
def calc_player_score(player_cards_list, player: str) -> int:
    score_count = 0
    ace_count = 0

    # Iterate over list of dict
    for player_dict in player_cards_list:
        # If player in dict
        if player in player_dict:
            # Access dict of cards in player dict
            for card_dict in player_dict.values():
                # Iterate over card names in card_dict
                for card in card_dict.keys():
                    # Check number of aces
                    if 'Ace' in card:
                        ace_count += 1

                # Iterate over card values in card_dict
                for score in card_dict.values():
                    score_count += score

            # After going through all cards in player dict, check aces
            # If 2 aces, return score of 21
            if ace_count == 2:
                score_count = 21
                return score_count

            # If not, return the score count as calculated
            else:
                return score_count

# Calculate current score of bank
def calc_bank_score(bank_cards_dict) -> int:
    score_count = 0
    ace_count = 0

    # Iterate over keys
    for card in bank_cards_dict.keys():
        # Check number of aces
        if 'Ace' in card:
            ace_count += 1

    # If 2 aces, return score of 21
    if ace_count == 2:
        score_count = 21
        return score_count
    # Otherwise iterate through dict, add up values and return score
    else:
        for score in bank_cards_dict.values():
            score_count += score
        return score_count


# Check, if a player has won or lost
def check_winner(current_total, player_cards_list, remaining_players, players_in, player) -> bool:

    # Check, if bank or player won or lost
    if current_total == 21:
        # Declare winner and end game
        calc_decl_winner(player_cards_list, remaining_players)
    elif current_total > 21:
        # Remove player from participating players
        remaining_players.remove(player)
        # Remove player from players being asked for cards
        players_in.remove(player)
        print(f"{player} passed 21 points and is no longer in the game.\n")

    else:
        # If player has neither won nor lost, return False, so it can be checked in y/n questions
        return False


# Calc final scores, find and declare winner
def calc_decl_winner(player_cards_list, remaining_players) -> None:

     # Initialize final scores dict
    final_scores = {}

    # Iterate over list of score dictionaries
    for player_dict in player_cards_list:
        for player, scores in player_dict.items():
            if isinstance(scores, dict):
                total_score = sum(scores.values())
            else:
                total_score = scores

            # Add total score to final scores dict
            if (player in final_scores) and (player in remaining_players):
                final_scores[player] += total_score
            elif player in remaining_players:
                final_scores[player] = total_score

    # Find the maximum score
    max_score = max(final_scores.values())

    # Collect all players with max score
    winner = [p for p, s in final_scores.items() if s == max_score]

    for w in winner:
        if w in remaining_players:
            print(f"{w} won with {max_score} points.\n")

    # End game
    sys.exit(0)

def main():

    # Initialize set of cards
    card_set = initialize_card_set()

    # Start game and initialize players
    player_names = initialize_players(4)

    # Initialize list to check, who's still in the game (i.e. not over 21)
    remaining_players = player_names.copy()

    # Initiate checkpoint, for players who still want cards
    players_in = remaining_players.copy()

    # Initialize list of player dicts cont. a dict with drawn cards and points
    # Example: [{'Mia': {'7 of hearts': 7}}, {'Tom': {'8 of diamonds': 8}}]
    player_cards_list =[{name: 0} for name in player_names]

    # Initialize dict holding cards of bank and their points
    bank_cards_dict = {}

    # Pause for a moment
    time.sleep(0.5)

    # Draw first card for bank and remove card from card set
    print("\nThe bank receives the first card.\n")
    card_name, card_score = draw_card(card_set)

    # Print the card drawn and its score --- Remove later ---
    print(f"The bank receives: {card_name}, Score: {card_score}. \n")

    # Update bank score dict
    update_bank_cards(bank_cards_dict, card_name, card_score)

    # Pause for a moment
    time.sleep(0.5)

    # Draw 2 cards per player, update player cards list and check, if no winner:
    print(f"Each player receives two cards.\n")

    # Iterate through players and give card two times
    for player in remaining_players:
        for _ in range(2):
            card_name, card_score = draw_card(card_set)
            update_player_cards(player_cards_list, player, card_name, card_score)
            print(f"{player} receives {card_name} ({card_score} points).")

            # Pause for a moment
            time.sleep(0.5)

        # Check & print current score of player
        current_total = calc_player_score(player_cards_list, player)
        print(f"{player}'s current total: {current_total}.\n")

        # Check, if player won or lost
        check_winner(current_total, player_cards_list, remaining_players, players_in, player)

    # While no winner and remaining players ask players - one by one - if they want a card, draw, check scores, repeat

    while True:
        # Iterable mustn't change
        for player in player_names:
            # Pause for a moment
            time.sleep(0.5)

            while True:
                if player in players_in and player in remaining_players:

                    want_card = input(f"{player}, would you like to draw another card (y/n)? ").lower()
                    print("")

                    # If yes, draw card, update score list and card set and move on to next player
                    if want_card == 'y':
                        card_name, card_score = draw_card(card_set)
                        update_player_cards(player_cards_list, player, card_name, card_score)
                        current_total = calc_player_score(player_cards_list, player)
                        print(f"{player} recieves {card_name} ({card_score} points).")
                        print(f"{player}'s current total: {current_total}.\n")

                        # Check, if player won or lost
                        # If winner, ends game
                        check_winner(current_total, player_cards_list, remaining_players, players_in, player)

                        # Move on to next player
                        break

                    # If answer 'n', remove player from players_in and move on to next player
                    elif want_card == 'n':
                        players_in.remove(player)
                        # Break inner while loop and move on to next player
                        break

                    # If neither, error message and go to start
                    else:
                        print("Input invalid. Try again.")
                        continue

                # If player not in remaining_players and players_in move on to next player
                else:
                    break

        # Pause
        time.sleep(0.5)

        # If nobody has won and nobody wants another card, stop outer while-loop
        if not players_in:
            print(f"The players' round is complete.\n")
            break

    # Pause
    time.sleep(0.5)

    # If no remaining players AND no winner, declare bank as winner
    if not remaining_players:
        print(f"All players have lost. The bank wins.\n")
        sys.exit(0)

    # Otherwise, start bank round
    print(f"The bank now draws its cards.\n")

    while True:
        # Draw card for bank
        card_name, card_score = draw_card(card_set)

        # Print the card drawn and its score  --- Remove later ---
        print(f"The bank receives: {card_name}, Score: {card_score}.\n")

        # Update bank cards dict
        update_bank_cards(bank_cards_dict, card_name, card_score)

        # Check, if bank has won or lost
        current_score = calc_bank_score(bank_cards_dict)
        # If bank won, declare as winner and end game
        if current_score == 21:
            print(f"The bank won the game. All other players loose.\n")
            sys.exit(0)
        # If bank has lost, end loop and proceed to declare winner
        elif current_score > 21:
            print(f"The bank lost with {current_score} points.\n")
            break
        # If bank has neiter won nor lost, draw next card
        else:
            time.sleep(0.5)
            continue

    # Declare winner
    calc_decl_winner(player_cards_list, remaining_players)


if __name__ == "__main__":
    main()
