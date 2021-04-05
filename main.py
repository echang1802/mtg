
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
    print(com)
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
    print(com)
    mtg.estimate_combination_of_cards_with_mulligans(deck, com)

    N = 1
    M = 4
    print("\nProbability of get M({}) lands in T turns when N({}) lands are drawed in first hand:".format(M,N))
    mtg.estimate_turns_until_M_lands(deck, N, M)
