
import mtg
from sys import argv

if __name__ == "__main__":

    deck = mtg.read_deck(argv[1])

    print(deck.cards())
    print(deck.cards_in_hand())
    deck.draw_hand()
    print(deck.cards_in_hand())
    print(deck.cards())
    deck.reset()
    print(deck.cards())
    print(deck.cards_in_hand())
