import random

suits = ['clubs', 'spades', 'diamonds', 'hearts']
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13,
          'Ace': 1}

war_stake = 5


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self):

        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # create a Card object and append in the deck object
                self.all_cards.append(Card(suit, rank))

    def deal(self):

        return self.all_cards.pop()

    def shuffle(self):
        random.shuffle(self.all_cards)

    def __len__(self):
        return len(self.all_cards)


class HandDeck:

    def __init__(self, name):

        self.name = name
        self.cards = []

    def play(self):
        return self.cards.pop(0)

    def win_round(self, new_cards):

        # We can win a single card or multiple card.
        # Single card will be a single card object
        # Multiple cards will be a list.
        # list should be extended to a list
        # single card should be appended
        # check if the input is a list or not

        if isinstance(new_cards, list):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)

        # print(f"Player {self.name} wins this round")

    def __str__(self):
        return f"Player{self.name} has {len(self.cards)} cards."

    def __len__(self):
        return len(self.cards)


# Deck object instance
deck = Deck()

# Deck shuffle
deck.shuffle()

# Create 2 hands full of cards
hand1 = HandDeck('Bappy')
hand2 = HandDeck('Jose')

# Deal cards to both players one by one
# win method of HandDeck class adds card to the current list
# deal at the beginning
for n in range(int(len(deck) / 2)):
    hand1.win_round(deck.deal())
    hand2.win_round(deck.deal())

game_on = True
r = 0
while game_on:

    r += 1
    print(f"Round {r}")

    # players play 1 card each to the board
    board = []
    board.append(hand1.play())
    print(f"player 1 plays {board[-1]}")
    board.append(hand2.play())
    print(f"player 2 plays {board[-1]}")

    # If any player runs out of cards. Game exits declaring one winner.
    if len(hand2) == 0:
        print(f"Player {hand1.name}: {len(hand1)} cards\nPlayer {hand2.name}: {len(hand2)} cards.")
        print(f"Player {hand1.name} wins!")
        game_on = False
        break

    if len(hand1) == 0:
        print(f"Player {hand1.name}: {len(hand1)} cards\nPlayer {hand2.name}: {len(hand2)} cards.")
        print(f"Player {hand2.name} wins!")
        game_on = False
        break

    war_on = True

    while war_on:

        # check hand 1 > hand 2, or hand 1 < hand 2 or hand 1 == hand 2
        # if someone wins, add the card(s) from the board cards to the winners deck
        # while loop exits for the next round

        # board[-1] is played by player 2
        if board[-1].value > board[-2].value:  # condition for player 2 win
            hand2.win_round(board)
            war_on = False  # Proceed to next round

        elif board[-1].value < board[-2].value:  # condition for player 1 win
            hand1.win_round(board)
            war_on = False  # Proceed to next round

        else:  # condition for TIE/WAR
            print("We are at WAR!")

            # check if players have enough cards to go to the war.

            # if BOTH DOESN"T HAVE ENOUGH CARDS in hand.
            if len(hand1) < war_stake and len(hand2) < war_stake:

                # PLayer 1 less than 5 cards, Player 1 has more than Player 2
                if len(hand1) > len(hand2):

                    print(f"Player {hand1.name}: {len(hand1)} cards\nPlayer {hand2.name}: {len(hand2)} cards.")
                    print(f"Player {hand1.name} wins!")
                    game_on = False
                    break

                # Player 2 less than 5 cards, but Player 2 has more than Player 1
                elif len(hand1) < len(hand2):

                    print(f"Player {hand1.name}: {len(hand1)} cards\nPlayer {hand2.name}: {len(hand2)} cards.")
                    print(f"Player {hand2.name} wins!")
                    game_on = False
                    break

                # Both players have less than 5 cards and equal number of cards, game is tied and the game exits.
                else:

                    print(f"Game Tied! You both have {len(hand1)} cards in hand")
                    game_on = False
                    break

            # If only PLAYER 2 HAS LESS THAN ENOUGH CARDS in hand
            elif len(hand2) < war_stake:
                print(f"Player {hand1.name}: {len(hand1)} cards\nPlayer {hand2.name}: {len(hand2)} cards.")
                print(f"Player {hand1.name} wins!")
                game_on = False
                break

            # If only PLAYER 1 HAS LESS THAN ENOUGH CARDS in hand
            elif len(hand1) < war_stake:
                print(f"Player {hand1.name}: {len(hand1)} cards\nPlayer {hand2.name}: {len(hand2)} cards.")
                print(f"Player {hand2.name} wins!")
                game_on = False
                break

            else:
                # Both have enough cards and war is on.
                # add 5 more cards to the board from each player.
                # then move for next round of card play.

                for n in range(war_stake):
                    board.append(hand1.play())
                    board.append(hand2.play())
