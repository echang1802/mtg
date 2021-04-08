# Magic the gathering

In this repo I will handle some stats to help upgrade my MTG: Arena performance.

### Deck stats

This module answer 5 important questions in deck building:

* Probability of draw N lands in the opening hand.
* Probability of draw N lands in the opening hand, open by color.
* Probability of a combination of cards in the opening hand.
* Probability of first occurrence  of a combination of cards in the opening hand open by mulligans.
* Given that N lands were drawn in the opening hand (without mulligans) how many turns will it take to draw M lands.

To use this module the deck to analyze should be recorded in a file as the `test_deck` example and use the following command line:

```
python main.py [deck_name]
```
