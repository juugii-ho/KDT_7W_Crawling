from card import Card
from player import Player
from gamedealer import GameDealer

def cardPrint(player1):
    print(f'{player1} Open Card list: {len(player1.open_card_list)}')
    for p in player1.open_card_list:
        print(p, end=' ')
    print('\n\n')
    print(f'{player1} Holding Card list: {len(player1.holding_card_list)}')
    for p in player1.holding_card_list:
        print(p, end=' ')
    print('\n\n')
    print("="*50)



def play_game():
    # 두 명의 player 객체 생성
    player1 = Player("흥부")
    player2 = Player("놀부")
    dealer = GameDealer()

    dealer.make_deck()
    dealer.shuffle_deck()
    dealer.game_start(player1,player2, 10)
    dealer.show_deck()
    print("="*50)
    cardPrint(player1)
    cardPrint(player2)
    inp = input("[2]단계: 다음 단계 진행을 위해 Enter 키를 누르세요! \n")
    if inp == "":
        print("=" * 50)
        print("[흥부: 숫자가 같은 한쌍의 카드 검사]")
        player1.check_one_pair_card()
        print("=" * 50)
        cardPrint(player1)
        print("[놀부: 숫자가 같은 한쌍의 카드 검사]")
        player2.check_one_pair_card()
        print("=" * 50)
        cardPrint(player2)
    else:
        print("종료하겠습니다.")

    def onepair(player):
        print(f"[{player}: 숫자가 같은 한쌍의 카드 검사]")
        print("=" * 50)

    i= 3
    for index in range(i,i+4):
        inp2 = input(f"[{i}]단계: 다음 단계 진행을 위해 Enter 키를 누르세요!")
        if inp2 == "":
            dealer.game_start(player1,player2, 4)
            dealer.show_deck()
            print("="*50)
            onepair(player1)
            player1.check_one_pair_card()
            cardPrint(player1)
            onepair(player2)
            player2.check_one_pair_card()
            cardPrint(player2)
        else:
            print("종료하겠습니다.")
        i+=1


if __name__ == '__main__':
    play_game()