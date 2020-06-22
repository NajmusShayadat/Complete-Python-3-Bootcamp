"""
Milestone Project 2 - Blackjack Game
In this milestone project you will be creating a Complete BlackJack Card Game in Python.

Here are the requirements:

You need to create a simple text-based BlackJack game
The game needs to have one player versus an automated dealer.
The player can stand or hit.
The player must be able to pick their betting amount.
You need to keep track of the player's total money.
You need to alert the player of wins, losses, or busts, etc...
And most importantly:

You must use OOP and classes in some portion of your game. You can not just use functions in your game. Use classes
to help you define the Deck and the Player's hand. There are many right ways to do this, so explore it well!
"""

import random

# global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10,
          'Ace': 11}

game_on = True


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    # Return string of card class
    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(rank, suit))

    def __str__(self):
        deck_set = ''
        for card in self.all_cards:
            deck_set += ('\n' + str(card))

        return 'This deck has \n\n' + deck_set

    def deal(self):
        return self.all_cards.pop()

    def shuffle_cards(self):
        random.shuffle(self.all_cards)


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def card_add(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.suit == 'Ace':
            self.aces += 1

    def ace_adjust(self):
        while self.value > 21 and self.aces:
            self.value += (-10)
            self.aces += (-1)


class Chips:

    def __init__(self):
        self.balance = 100
        self.bet = 0

    def win(self):
        self.balance += self.bet

    def lose(self):
        self.balance -= self.bet


def take_bet(chips):

    # Bet cannot exceed the balance and bet must be an integer.
    while True:
        try:
            chips.bet = int(input(f'\nYour Chips balance is {chips.balance}.\nHow much do you want to bet? '))
        except ValueError:
            print('\nMust be an integer input!')
        else:
            if chips.bet > chips.balance:
                print(f"\nYou can't exceed {chips.balance}!")
            elif chips.bet < 1:
                print("\nPlease bet more than 0! ")
            else:
                break


def hit(deck1, hand):
    hand.card_add(deck1.deal())
    hand.ace_adjust()


def hit_or_stand(deck1, hand):
    global game_on

    while True:
        x = input("\nHit or Stand? Enter h or s: ")
        if x[0].lower() == 'h':
            hit(deck1, hand)
        elif x[0].lower() == 's':
            print('\nPlayer stands!')
            game_on = False
        else:
            print("\nPlease enter h for Hit or s for Stand.")
            continue
        break


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(f"\t{dealer.cards[0]}")
    print("\t<Hidden Card>")

    print("\nPlayer's Hand:", *player.cards, sep='\n\t')
    print("Player's total: ", player.value)


def show_all(player, dealer):
    print("\nDealer's Hand: ", *dealer.cards, sep='\n\t')
    print("Dealer's total: ", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep='\n\t')
    print("Player's total: ", player.value)


def player_busts(chips):
    print("\nPlayer Busted!")
    chips.lose()


def player_wins(chips):
    print("\nPlayer wins!")
    chips.win()


def dealer_busts(chips):
    print("\nDealer Busted!")
    chips.win()


def dealer_wins(chips):
    print("\nDealer wins!")
    chips.lose()


def push():
    print("\nScore tie's, it's a push!")


# Game Starts
# Create initial balance of the chips
player_chips = Chips()

while True:

    print(
        'Welcome to BlackJack! Get as close to 21 as you can without going over!\nDealer hits until she reaches 17. '
        'Aces count as 1 or 11.')

    deck = Deck()
    deck.shuffle_cards()

    player_hand = Hand()
    # Deal 2 cards for player
    player_hand.card_add(deck.deal())
    player_hand.card_add(deck.deal())

    dealer_hand = Hand()
    # Deal 2 cards for dealer
    dealer_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while game_on:

        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_chips)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)
        else:
            push()

    print(f"\nPlayer's balance is {player_chips.balance}")

    # Check the final balance is more than 0 and then ask for replay.
    if player_chips.balance != 0:
        new_game = input("\nWould you like to play again? Enter y/n: ")
        if new_game[0].lower() == 'y':
            game_on = True
            continue
        else:
            print("\nThanks for playing!")
            break

    else:
        print(f"\nYour chips balance is Zero (0).\nThank you for playing!")
        break
