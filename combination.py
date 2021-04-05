
from deck import land, spell

class combo:

    def __init__(self, combinations):
        self._cards = []

        for card_type in combinations.keys():
            for color in combinations[card_type].keys():
                if card_type == "lands":
                    for i in range(combinations[card_type][color]):
                        self._cards.append(land([color]))
                else:
                    for cost in combinations[card_type][color].keys():
                        for i in range(combinations[card_type][color][cost]):
                            self._cards.append(spell(int(cost), [color], card_type))

    def __contains__(self, hand):
        for c in self._cards:
            is_in = False
            for h in hand:
                is_in = h == c
                if is_in:
                    break
            if not is_in:
                return False
        return True

    def cards_in_combo(self):
        return len(self._cards)
