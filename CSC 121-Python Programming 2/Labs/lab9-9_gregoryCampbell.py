# Gregory Campbell  lab 9-9     February 14, 2022
"""
    This program uses a dictionary as a deck of cards and simulates a simplified
    version of Blackjack between two players. The program deals cards to each player
    until one player's hand is worth more than 21 points. When that happens the other
    player wins. If both players exceed 21 points neither player wins. The program
    repeats until all the cards have been dealt. If an player is dealt an ace, the 
    program should decide the value of the card: the ace is worth 11 points unless 
    that makes the hand exceed 21 otherwise it is worth 1 point.
"""
import random

#========================= main method
def main():
    # Create a deck of cards.
    deck = create_deck()

    # Initialize accumulators for the players' hand values, win-loss records.
    player_one_hand_value = 0
    player_two_hand_value = 0
    player_one_wins = 0
    player_two_wins = 0
    no_player_wins = 0

    # Display header for output
    display_header()
    # Begin loop that continues until all cards are dealt.
    while len(deck) > 0:

        # deal first round of cards
        display_player_header('Player One:')
        player_one_hand_value = deal_cards(player_one_hand_value, deck, 2, player_one_wins, player_two_wins, no_player_wins)
        display_player_header('Player Two:')
        player_two_hand_value = deal_cards(player_two_hand_value, deck, 2, player_one_wins, player_two_wins, no_player_wins)

        # keep dealing cards until one player or both go over 21
        while player_one_hand_value <= 21 and player_two_hand_value <=22:
            display_player_header('Player One:')
            player_one_hand_value = deal_cards(player_one_hand_value, deck, 1, player_one_wins, player_two_wins, no_player_wins)
            display_player_header('Player Two:')
            player_two_hand_value = deal_cards(player_two_hand_value, deck, 1, player_one_wins, player_two_wins, no_player_wins)

            # determine winner if applicable
            if player_one_hand_value <= 21 and player_two_hand_value > 21:
                print('     Player One wins!\n')
                print('____________________________\n')
                player_one_wins += 1
                break
            elif player_one_hand_value > 21 and player_two_hand_value <= 21:
                print('     Player Two wins!\n')
                print('____________________________\n')
                player_two_wins += 1
                break
            elif player_one_hand_value > 21 and player_two_hand_value > 21:
                print('   Neither player wins.\n')
                print('____________________________\n')
                no_player_wins += 1
                break
        
        # begin next hand, re-initializing players' hand values
        print('       Next hand:\n')
        player_one_hand_value = 0
        player_two_hand_value = 0
            
    # if all cards are dealt, display win-loss record,say goodbye
    display_records(player_one_wins, player_two_wins, no_player_wins)
    display_goodbye_message()

#======================== methods
# The create_deck function returns a dictionary representing a deck of cards.
def create_deck():
    # Create a dictionary with each card and its value stored as key-value pairs.
    deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,
            
            'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts': 10,
            
            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs': 10,
            
            'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds': 10}

    # Return the deck.
    return deck

# display_header displays a header for the output
def display_header():
    print('\n    BlackJack Simulator')
    print('===========================\n')


# display_player_header displays each player's header in output
def display_player_header(player):
    print(f'{player}')
    print('-----------')

# The deal_cards function deals a specified number of cards from the deck.
def deal_cards(hand_value, deck, number, player_one_wins, player_two_wins, no_player_wins):
    # Make sure the number of cards to deal is not greater than the number of cards in the deck.
    # Exit the program, if so.
    if number > len(deck):
        print('\nHand canceled!\n')
        display_records(player_one_wins, player_two_wins, no_player_wins)
        exit()

    # Deal the cards and accumulate their values.
    for count in range(number):
        card = random.choice(list(deck))
        print(card)
        card_value = deck[card]

        # if the card drawn is an ace, determine its value based on hand_value
        if card_value == 1:
            card_value = choose_ace_value(hand_value)

        # accumulate hand value
        hand_value += card_value

        # remove the randomly-selected card from the deck
        del deck[card]

    # Display the value of the hand.
    print(f'Value of this hand: {hand_value}\n')

    return hand_value

# choose_ace_value decides the value of an ace
def choose_ace_value(hand_value):
    # ace is worth 11 unless that makes hand_value exceed 21, in which case ace is worth 1.
    ACE_VALUE = 11
    if (ACE_VALUE + hand_value) > 21:
        return 1
    else:
        return 11

# display_records shows accumulated wins/no winners
def display_records(player_one_wins, player_two_wins, no_player_wins):
    print('No more cards to deal!\n\n')
    print('-----------Results-----------')
    print(f'\nPlayer One wins: {player_one_wins}\nPlayer Two wins: {player_two_wins}\nNo winner: {no_player_wins}\n')


# display_goodbye_message confirms program has ended because the deck is out of cards
def display_goodbye_message():
    print("\nThank you for using this program. Goodbye!\n")

#========================= Call the main function.
if __name__ == '__main__':
    main()