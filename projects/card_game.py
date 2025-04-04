# create classes that model a card game
# use classes to build a game

import random

rank_values = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14
}
        
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = rank_values[rank]
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __lt__(self, other):
        return self.value < other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __eq__(self, other):
        return self.value == other.value
    
class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        ranks = rank_values.keys() #["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        player1_cards = []
        player2_cards = []
        while self.cards:
            # if self.cards:
            player1_cards.append(self.cards.pop())
            # if self.cards:
            player2_cards.append(self.cards.pop())
            # because of even number of cards, always be able to pop two cards if there are cards in the deck (assuming if you have even cards in the deck)
            # Because of evenness, you will ensure you will end up on line 66 with the last card
        return player1_cards, player2_cards
    
class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        if self.hand:
            return self.hand.pop()
        else:
            return None
        
    def play_war_cards(self):
        war_cards = []
        while self.hand and len(war_cards) < 3:
            war_cards.append(self.hand.pop())
        # if len(self.hand) >= 3:
        #     return [self.hand.pop(), self.hand.pop(), self.hand.pop()]
        # elif len(self.hand) == 2:
        #     return [self.hand.pop(), self.hand.pop()]
        # elif len(self.hand) == 1:
        #     return [self.hand.pop()]
        return war_cards
            
    # def player_cards(self, player_number):
    #     self.player_number = player_number

    def add_cards(self, cards):
        if isinstance(cards, list):
            self.hand = cards + self.hand
        else:
            self.hand.insert(0, cards)

class WarGame:
    def __init__(self, player1_name, player2_name):
        deck = Deck()
        deck.shuffle()
        hand1, hand2 = deck.deal()
        self.player1 = Player(player1_name, hand1)
        self.player2 = Player(player2_name, hand2)

    def card_comparison(self, card1, card2, cards_played):
        if card1 is None or card2 is None:
            return False
        elif card1 > card2:
            print(f"{self.player1.name} wins the round!\n")
            self.player1.add_cards(cards_played)
        else:
            print(f"{self.player2.name} wins the round!\n")
            self.player2.add_cards(cards_played)
    
    def set_hands(self, player1_hand, player2_hand):
        self.player1.hand = player1_hand
        self.player2.hand = player2_hand

    def play_round(self):
        card1 = self.player1.play_card()
        card2 = self.player2.play_card()

        if card1 is None or card2 is None:
            return False

        print(f"{self.player1.name} plays: {card1}")
        print(f"{self.player2.name} plays: {card2}")

        cards_played = [card1, card2]

        if card1 == card2:
            print("WAR!")
            war_round_cards, card1, card2 = self.war()
            cards_played += war_round_cards
        self.card_comparison(card1, card2, cards_played)
        return
    
    def war(self):
        player1_war_cards = self.player1.play_war_cards()
        player2_war_cards = self.player2.play_war_cards()
        
        # Need to check if each player has cards remaining
        if not player1_war_cards or not player2_war_cards:
            return player1_war_cards + player2_war_cards, None, None
        
        player1_flipped_war_card = player1_war_cards[-1]
        player2_flipped_war_card = player2_war_cards[-1]
        if player1_flipped_war_card == player2_flipped_war_card:
            print("WAR continues!")
            next_round_cards, next_player1_card, next_player2_card = self.war()
            return player1_war_cards + player2_war_cards + next_round_cards, next_player1_card, next_player2_card
        return player1_war_cards + player2_war_cards, player1_flipped_war_card, player2_flipped_war_card
    
    def game_over(self):
        return len(self.player1.hand) == 0 or len(self.player2.hand) == 0
    
    def play_auto(self, max_rounds = 10000):
        round_counter = 0
        while not self.game_over():
            if round_counter >= max_rounds:
                print("You've reached the max number of rounds")
                return
            print(f"{self.player1.name} has {len(self.player1.hand)} cards.\n{self.player2.name} has {len(self.player2.hand)} cards.\n")
            round_counter += 1
            print(f"\n---Round {round_counter}---")
            self.play_round() 
        print("Game Over!")
        if len(self.player1.hand) > len(self.player2.hand):
            print(f"{self.player1.name} wins!")
        else:
            print(f"{self.player2.name} wins!")

    def play(self):
        round_counter = 0
        while not self.game_over():
            user_input = ""
            while user_input != "f" or user_input != "c":
                user_input = input("Enter 'f' to flip card for next round or 'c' to check number of cards in each hand: ")
                if user_input == "f":
                    round_counter += 1
                    print(f"\n---Round {round_counter}---")
                    self.play_round()
                elif user_input == "c":
                    print(f"{self.player1.name} has {len(self.player1.hand)} cards.\n{self.player2.name} has {len(self.player2.hand)} cards.\n")
        print("Game Over!")
        if len(self.player1.hand) > len(self.player2.hand):
            print(f"{self.player1.name} wins!")
        else:
            print(f"{self.player2.name} wins!")

if __name__ == "__main__":
    player1 = input("Player 1 - Enter your name: ")
    play_against_computer = input("Play against the computer? Enter y/n: ")
    if play_against_computer.lower() in ["y", "yes"]:
        player2 = "Computer"
    else:
        player2 = input("Player 2 - Enter your name: ")
    print()
    game = WarGame(player1, player2)
    game.play_auto()
    
    # how to play game
    # method to check to see who won
    # could write game loop in script
    # method also in WarGame, with play function

