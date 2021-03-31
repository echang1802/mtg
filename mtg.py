
import deck

def read_deck(filename):
    with open(filename, "r") as file:
        cards_descriptions = file.readlines()

    new_deck = deck.deck()

    for c in cards_descriptions:
        description = eval(c)
        if description["type"] == "land":
            new_deck.add_lands(int(description["number"]), description["tapped"], description["colors"])
        elif description["type"] == "spell":
            new_deck.add_spells(description["sub_type"], description["costs"], description["colors"])

    if new_deck.cards() < 60:
        print("Deck is not complete")

    return new_deck

def estimate_lands_in_fist_hand(deck, simulations = 1000):
    counts = {}
    for s in range(simulations):
        deck.draw_hand()
        lands = deck.cards_type_in_hand("land")
        if str(lands) in counts.keys():
            counts[str(lands)] += 1
        else:
            counts[str(lands)] = 1
        deck.reset()
    return counts
