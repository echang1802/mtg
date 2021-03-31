
import mtg
from sys import argv

if __name__ == "__main__":

    deck = mtg.read_deck(argv[1])

    distribution = mtg.estimate_lands_in_fist_hand(deck)

    print(distribution)
