##### Deck Class #####

# Create a Deck class that represents a deck of 52 playing cards.  The Deck should maintain which cards 
# are currently in the deck and never contain duplicated cards.  Cards should be represented by a string 
# containing their value (2 - 10, J, Q, K, A) followed by their suit (D, H, C, S).  For example, the 
# jack of clubs would be represented by "JC" and the three of hearts would be represented by "3H".

# Your Deck class should implement the following methods:

##### shuffle(): This method shuffles the cards randomly, in place.
##### You may use the random.shuffle() method to help you do this.

##### deal(n): This method removes and returns the last n cards from the deck in a list.
##### If the deck does not contain enough cards, it returns all the cards in the deck.

##### sort_by_suit(): This method sorts the cards by suit, placing all the hearts first, diamonds 
##### second, clubs third and spades last.  The order within each suit (i.e. the card values) does 
##### not matter.  This method should sort the cards in place, it does not return anything.

##### contains(card): This method returns True if the given card exists in the deck and False otherwise.

##### copy(): This method returns a new Deck object that is a copy of the current deck.
##### Any modifications made to the new Deck object should not affect the Deck object that was copied.

##### get_cards(): This method returns all the cards in the deck in a list.
##### Any modifications to the returned list should not change the Deck object.

##### __len__(): This method returns the number of the cards in the Deck.

# Your deck should always start with exactly 52 cards that are distributed 
# across 4 suits and 13 values where there are no duplicate cards.

# See below for an example of how the Deck class should behave.

# >>> d = Deck()
# >>> d.shuffle()
# >>> d.deal(3)
# ["AS", "2H", "4D"]
# >>> d.contains("4D")
# False
# >>> d.sort_by_suit()
# >>> d.deal(3)
# ['2S', '5S', 'JS']
# >>> d.add_to_deck(["11H", "4D", "2S"])
# >>> len(d)
# 48

import random


class Deck:
    suits = ["H", "D", "C", "S"]
    values = [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]

    def __init__(self):
        self.cards = []
        self.fill_deck()

    def fill_deck(self):
        for suit in Deck.suits:
            for value in Deck.values:
                card = value + suit
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n):
        dealt_cards = []

        for i in range(n):
            if len(self.cards) == 0:
                break

            card = self.cards.pop()
            dealt_cards.append(card)

        return dealt_cards

    def sort_by_suit(self):
        cards_by_suit = {"H": [], "D": [], "C": [], "S": []}

        for card in self.cards:
            suit = card[-1]
            cards_by_suit[suit].append(card)

        self.cards = (
            cards_by_suit["H"] +
            cards_by_suit["D"] +
            cards_by_suit["C"] +
            cards_by_suit["S"]
        )

    def contains(self, card):
        return card in self.cards

    def copy(self):
        new_deck = Deck()
        new_deck.cards = self.cards[:]
        return new_deck

    def get_cards(self):
        return self.cards[:]

    def __len__(self):
        return len(self.cards)