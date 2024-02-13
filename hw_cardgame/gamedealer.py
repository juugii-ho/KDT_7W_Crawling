from card import Card
import random
from player import Player


class GameDealer:
    def __init__(self):
        self.deck = list()
        self.suit_number = 13
        self.popList = list()

    def make_deck(self):
        card_suits = ["♠", "♥", "♣", "◆"]
        card_numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for cs in card_suits:
            for cn in card_numbers:
                card = Card(cs,cn)
                self.deck.append(card)

    def show_deck(self):
        print(f"[GameDealer] 딜러가 가진 카드 수 : {len(self.deck)}")
        i = 1
        for d in self.deck:
            if i % 13 == 0:
                print(d)
            else:
                print(d, end=" ")
            i+=1
        print()

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def game_start(self, player1, player2, num):
        print("=" * 50)
        print(f'카드 나누어 주기 : {num}장')
        print("-" * 50)
        for p in range(num):
            pop = self.deck.pop()
            self.popList.append(pop)
        player1.add_card_list(self.popList)
        self.popList.clear()

        for p in range(num):
            pop = self.deck.pop()
            self.popList.append(pop)
        player2.add_card_list(self.popList)
        self.popList.clear()

