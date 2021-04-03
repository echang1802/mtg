
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

def print_distribution(dist):
    for k in dist.keys():
        print("{}:".format(k))
        if type(dist[k]) == dict:
            for k2 in dist[k].keys():
                print("\t{}:{}".format(k2,dist[k][k2]))
        else:
            print("\t{}".format(dist[k]))

def estimate_lands_in_fist_hand(deck, simulations = 1000):
    counts = {}
    for s in range(simulations):
        deck.draw_hand()
        lands = str(deck.cards_type_in_hand("land")["cards"])
        if lands in counts.keys():
            counts[lands] += 1
        else:
            counts[lands] = 1
        deck.reset()
    return counts

def estimate_lands_in_fist_hand_by_color(deck, simulations = 1000):
    counts = {}
    for s in range(simulations):
        deck.draw_hand()
        lands = deck.cards_type_in_hand("land")
        if str(lands["cards"]) in counts.keys():
            counts[str(lands["cards"])]["count"] += 1
            c =  "|".join(["{}:{}".format(c,lands["colors"][c]) for c in lands["colors"].keys()])
            if c in counts[str(lands["cards"])]["colors"].keys():
                counts[str(lands["cards"])]["colors"][c] += 1
            else:
                counts[str(lands["cards"])]["colors"][c] = 1
        else:
            counts[str(lands["cards"])] = {
                "count" : 1,
                "colors" : {
                    "|".join(["{}:{}".format(c,lands["colors"][c]) for c in lands["colors"].keys()]) : 1
                }
            }
        deck.reset()
    return counts
