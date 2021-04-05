
import deck
from combination import combo
from probability import distribution

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
    dist = distribution()
    for s in range(simulations):
        deck.draw_hand()
        lands = str(deck.cards_type_in_hand("land")["cards"])
        dist.add_data(lands)
        deck.reset()
    dist.show()

def estimate_lands_in_fist_hand_by_color(deck, simulations = 1000):
    dist = distribution()
    for s in range(simulations):
        deck.draw_hand()
        lands = deck.cards_type_in_hand("land")
        c =  "|".join(["{}:{}".format(c,lands["colors"][c]) for c in lands["colors"].keys()])
        dist.add_data(c)
        deck.reset()
    dist.show()

def estimate_combination_of_cards(deck, combination, simulations = 1000):
    counts = 0
    for s in range(simulations):
        deck.draw_hand()
        if deck.get_hand() in combination:
            counts += 1
        deck.reset()
    return counts / simulations

def estimate_combination_of_cards_with_mulligans(deck, combination, simulations = 1000):
    dist = distribution()
    for s in range(simulations):
        deck.draw_hand()
        combo_appear = deck.get_hand() in combination
        cards_restriction = deck.cards_in_hand() == combination.cards_in_combo()
        ready =  combo_appear or cards_restriction
        while not ready:
            deck.mulligan()
            combo_appear = deck.get_hand() in combination
            cards_restriction = deck.cards_in_hand() == combination.cards_in_combo()
            ready =  combo_appear or cards_restriction
        dist.add_data(deck.mulligans_taken() if combo_appear else -1)
        deck.reset()
    dist.show()
