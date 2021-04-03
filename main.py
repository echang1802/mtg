
import mtg
from sys import argv

if __name__ == "__main__":

    deck = mtg.read_deck(argv[1])

    distribution = mtg.estimate_lands_in_fist_hand(deck)
    mtg.print_distribution(distribution)

    distribution = mtg.estimate_lands_in_fist_hand_by_color(deck)
    mtg.print_distribution(distribution)
