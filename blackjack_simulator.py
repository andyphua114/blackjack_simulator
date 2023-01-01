from collections import namedtuple
import random


def shuffle_deck():
    card = namedtuple('card', ['value', 'suit'])
    suits = ['hearts', 'diamonds', 'spades', 'clubs']
    cards = [card(value, suit) for value in range(1, 11) for suit in suits]  # create ace to ten
    picture_cards = [card(10, suit) for value in range(3) for suit in suits]  # create jack to king as value 10
    cards.extend(picture_cards)
    random.shuffle(cards)
    return cards


if __name__ == '__main__':

    random.seed(6644)

    for i in range(1):
        deck = shuffle_deck()
        print(deck[0])
