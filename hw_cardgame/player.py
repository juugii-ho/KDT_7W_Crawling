class Player:
    def __init__(self, name):
        self.name= name
        self.holding_card_list = list()
        self.open_card_list = list()
        self.hdList=list()
        self.pophd=list()

    def __str__(self):
        return f'[{self.name}]'

    def add_card_list(self,card_list):
        self.holding_card_list.extend(card_list)

    def display_two_card_lists(self):
        for hd in self.open_card_list:
            print(hd, end=' ')

    def check_one_pair_card(self):
        for i in range(5):
            for index in range(len(self.holding_card_list)):
                for index2 in range(index+1,len(self.holding_card_list)):
                    if self.holding_card_list[index].number == self.holding_card_list[index2].number:
                        self.open_card_list.append(self.holding_card_list[index])
                        self.open_card_list.append(self.holding_card_list[index2])
                        self.holding_card_list.remove(self.holding_card_list[index])
                        self.holding_card_list.remove(self.holding_card_list[index2-1])
                        break



if __name__ == "__main__":
    test = Player("흥부")
    test.check_one_pair_card()



