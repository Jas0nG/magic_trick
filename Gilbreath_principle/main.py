# This is a demo of the Gilbreath principle in card magic.

import random

# Suit enum
dict_suit = {
    'Spades' : '\033[30m♠\033[0m',
    'Hearts' : '\033[91m♥\033[0m',
    'Clubs' : '\033[30m♣\033[0m',
    'Diamonds' : '\033[91m♦\033[0m'
}

list_ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.suit == other.suit and self.value == other.value
        return False

    def __str__(self):
        return f'{dict_suit[self.suit]}{self.value}'


class Deck:
    def __init__(self, name, cards = []):
        self.cards = cards
        self.name = name

    def build(self):
        for suit in dict_suit:
            for value in list_ranks:
                self.cards.append(Card(suit, value))

    def build_rbrb(self):
        for value in list_ranks:
            for suit in dict_suit:
                self.cards.append(Card(suit, value))

    def build_with_ranklist(self, list_rank):
        for value in list_rank:
            suit = 'Spades'
            if Card(suit, value) in self.cards:
                card_added = False
                for suit_new in dict_suit:
                    if Card(suit_new, value) not in self.cards:
                        self.cards.append(Card(suit_new, value))
                        card_added = True
                        break
                if not card_added:
                    print("[build_with_ranklist] The ranklist contains duplicate cards. with value: " + value)
                    exit(1)
            else:
                self.cards.append(Card(suit, value))
                


    def show(self):
        print(f"=====Deck: {self.name}=====")
        for card in self.cards:
            print(card, end=' ')
        print(f"\n{len(self.cards)} cards in total.")

    def show_col(self, col):
        print(f"=====Deck: {self.name}=====")
        for i in range(0, len(self.cards), col):
            for j in range(col):
                if i + j < len(self.cards):
                    print(self.cards[i + j], end=' ')
            print()
        print(f"\n{len(self.cards)} cards in total.")

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def riffle_shuffle(self, another_deck = None):
        if another_deck is None:
            half = len(self.cards) // 2
            shuffled = []
            for i in range(half):
                shuffled.append(self.cards[i])
                shuffled.append(self.cards[i + half])
            self.cards = shuffled
        else:
            if len(self.cards) != len(another_deck.cards):
                print("[riffle_shuffle] The two decks have different number of cards. deck1: " + str(len(self.cards)) + " deck2: " + str(len(another_deck.cards)))
                exit(1)
            shuffled = []
            for i in range(len(self.cards)):
                shuffled.append(self.cards[i])
                shuffled.append(another_deck.cards[i])
            self.cards = shuffled

    def riffle_shuffle_noob(self, another_deck = None):
        if another_deck is None:
            pass
        else:
            shuffled = []
            # 实现不均匀的riffle_shuffle
            deck_count = 0
            another_deck_count = 0
            while (deck_count < len(self.cards) and another_deck_count < len(another_deck.cards)):
                if random.random() < 0.5:
                    shuffled.append(self.cards[deck_count])
                    deck_count += 1
                else:
                    shuffled.append(another_deck.cards[another_deck_count])
                    another_deck_count += 1
            if deck_count < len(self.cards):
                shuffled += self.cards[deck_count:]
            if another_deck_count < len(another_deck.cards):
                shuffled += another_deck.cards[another_deck_count:]
            self.cards = shuffled
            self.name += " and " + another_deck.name + " shuffled"

    def cut_into_two(self):
        half = len(self.cards) // 2
        return self.cards[:half], self.cards[half:]

    def cut_into_two_deck(self):
        half = len(self.cards) // 2
        return Deck("1st half of " + self.name, self.cards[:half]), Deck("2nd half of "+ self.name, self.cards[half:])
    
    def reverse(self):
        self.cards = self.cards[::-1]

# End of class design

def red_black_trick():
    deck_A = Deck("A")
    deck_A.build_rbrb()
    print("Original deck:")
    deck_A.show()
    half1, half2 = deck_A.cut_into_two()
    deck_A_1 = Deck("1st half of A", half1)
    deck_A_2 = Deck("2nd half of A", half2)
    deck_A_1.reverse()
    print("Cut deck and reverse the 1st half")
    deck_A_1.show()
    deck_A_2.show()
    print("Riffle shuffle the two halves, not a perfect shuffle")
    deck_A_1.riffle_shuffle_noob(deck_A_2)
    deck_A_1.show_col(2)

def the_answer():
    loop_rank = ['A', 'K', '2', 'Q', '3', 'J', '4', '10', '5', '9', '6', '8']
    whole_deck = []
    whole_deck.extend(loop_rank)
    whole_deck.extend(loop_rank)
    whole_deck.extend(loop_rank)
    whole_deck.extend(loop_rank)
    whole_deck.extend(['7','7','7','7'])
    deck = Deck("A")
    deck.build_with_ranklist(whole_deck)
    deck.show()

    deck_1, deck_2 = deck.cut_into_two_deck()
    deck_1.show()
    deck_2.show()
    deck_1.reverse()
    deck_1.riffle_shuffle_noob(deck_2)
    deck_1.show_col(6)

def test_gp():
    custom_rank = ['A', '2', '3', '4', '5']
    whole_deck = []
    whole_deck.extend(custom_rank)
    whole_deck.extend(custom_rank)
    whole_deck.extend(custom_rank)
    whole_deck.extend(custom_rank)
    deck = Deck("A")
    deck.build_with_ranklist(whole_deck)
    deck.show()
    deck_1, deck_2 = deck.cut_into_two_deck()
    deck_1.reverse()
    deck_1.show()
    deck_2.show()
    deck_1.riffle_shuffle_noob(deck_2)
    deck_1.show_col(5)


if __name__ == "__main__":
    # red_black_trick()
    the_answer()
    # test_gp()
