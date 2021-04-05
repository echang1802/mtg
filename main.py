
import mtg
from sys import argv

if __name__ == "__main__":

    deck = mtg.read_deck(argv[1])

    print("Probability of land in first hand:")
    mtg.estimate_lands_in_fist_hand(deck)

    print("\nProbability of land in first hand by color:")
    mtg.estimate_lands_in_fist_hand_by_color(deck)

    print("\nProbability of combination in first hand:")
    combination = {
        "lands" : {
            "white" : 1,
            "black" : 1
        },
        "creature": {
            "white" : {
                "1" : 1,
                "2" : 1
            },
            "black" : {
                "1" : 1
            }
        }
    }
    com = mtg.combo(combination)
    counts = mtg.estimate_combination_of_cards(deck, com)
    print("{}%".format(counts))

    print("\nProbability of first appaearence of combination in mulligans:")
    combination = {
        "lands" : {
            "white" : 1,
            "black" : 1
        }
    }
    com = mtg.combo(combination)
    mtg.estimate_combination_of_cards_with_mulligans(deck, com)
