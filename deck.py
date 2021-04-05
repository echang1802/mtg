
from random import choice

class card:

    def __init__(self, type, colors):
        self.type = type
        self._colors = colors

    def colors(self):
        return "-".join(self._colors)

    def __repr__(self):
        return "{}-{}".format(self.type, "-".join(self._colors))

class land(card):

    def __init__(self, colors, enter_tapped = False):
        super().__init__("land", colors)
        self.enter_tapped = enter_tapped

    def __eq__(self, other):
        if other.type != "land":
            return False
        return other.colors() == self.colors() and other.enter_tapped == self.enter_tapped

class spell(card):

    def __init__(self, cost, colors, type):
        super().__init__(type, colors)
        self.cost = cost

    def __eq__(self, other):
        if other.type == "land":
            return False
        return other.type == self.type and other.cost == self.cost and  other.colors() == self.colors()

    def __repr__(self):
        return "{}-{}-{}".format(self.type, "-".join(self._colors), self.cost)

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

    def get_hand(self):
        return self._hand

    def cards_type_in_hand(self, type):
        if self.cards_in_hand() == 0:
            return {}
        counts = 0
        colors = {}
        for c in self._hand:
            if c.type == type:
                counts += 1
                if c.colors() in colors.keys():
                    colors[c.colors()] += 1
                else:
                    colors[c.colors()] = 1
        return {"cards": counts, "colors": colors}
