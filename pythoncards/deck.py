# I didn't like two python card deck library options so I decided to make my own which I'm calling "pythoncards".
import random


class Card:

    def __init__(self, suit: str, value: str or int):
        self.suit = suit
        self.value = value


# Deck class for creating a deck list that will work with the card class.
class Deck:

    def __init__(self, name: str, deck_count: int = 1, jokers: bool = False, existing_cards: list = None):
        self.name = name  # Name attribute, nothing special.

        # DISCARD VV
        if (name[0] == '"') and (name[-9:] == '"_discard') and (deck_count == 0):
            pass  # Doesn't do anything because this deck object is supposed to be a discard attribute for another deck object in itself.
        else:
            self.discard = Deck(f'"{name}"_discard', 0)  # Discard attribute defined as an empty deck object.
        # DISCARD ^^

        # CONTENT_&_JOKERS VV
        if jokers:
            self.content = [Card('red', 'joker'),
                            Card('black', 'joker')]  # I used colors for the joker's suits because the joker doesn't really have a suit.
        elif not jokers:
            self.content = []
        else:
            raise ValueError('pythoncards doesn\'t know whether or not to add jokers to the deck: expected boolean for the jokers attribute.')
        # CONTENT_&_JOKERS ^^

        # CUSTOM_LIST_OF_CARDS VV
        if existing_cards is None:  # If nothing is passed for existing_cards, it'll continue with the regular algorithm used for building the deck.

            # ADDING_CARDS VV
            if deck_count == 1:
                self.add_deck()
            elif deck_count > 1:
                self.add_deck(deck_count)
            else:
                raise ValueError('Deck count has to be a natural number; positive integer')
            # ADDING_CARDS ^^

        elif (existing_cards is not None) and (type(existing_cards) is list) and (deck_count is None):  # List of cards was passed as existing cards.
            self.content.extend(existing_cards)
        # CUSTOM_LIST_OF_CARDS ^^

    def add_deck(self, num_of_decks: int = 1):  # Method to add cards to a deck object (self) by the deck.
        suits = ['spades', 'hearts', 'clubs', 'diamonds']
        values = [*range(2, 11), 'jack', 'queen', 'king', 'ace']
        for d in range(num_of_decks):
            for card in values:
                for suit in suits:
                    self.content.append(Card(suit, card))
