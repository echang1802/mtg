
from random import choice

class card:

    def __init__(self, type, colors):
        self.type = type
        self.colors = colors

class land(card):

    def __init__(self, colors, enter_tapped):
        super().__init__("land", colors)
        self.enter_tapped = enter_tapped

class spell(card):

    def __init__(self, cost, colors, type):
        super().__init__(type, colors)
        self.cost = cost

class deck:

    def __init__(self):
        self._cards = []
        self._hand = []

    def add_lands(self, N, enter_tapped, colors):
        for i in range(N):
            self._cards.append(land(colors, enter_tapped))

    def add_spells(self, type, costs, colors):
        for cost in costs.keys():
            for i in range(costs[cost]):
                self._cards.append(spell(int(cost), colors, type))

    def draw(self):
        ind = choice(range(self.cards()))
        self._hand.append(self._cards[ind])
        self._cards.pop(ind)

    def draw_hand(self):
        for i in range(7):
            self.draw()

    def reset(self):
        for c in self._hand:
            self._cards.append(c)
        self._hand = []

    def cards(self):
        return len(self._cards)

    def cards_in_hand(self):
        return len(self._hand)

def read_deck(filename):
    with open(filename, "r") as file:
        cards_descriptions = file.readlines()

    new_deck = deck()

    for c in cards_descriptions:
        description = eval(c)
        if description["type"] == "land":
            new_deck.add_lands(int(description["number"]), description["tapped"], description["colors"])
        elif description["type"] == "spell":
            new_deck.add_spells(description["sub_type"], description["costs"], description["colors"])

    if new_deck.cards() < 60:
        print("Deck is not complete")

    return new_deck
