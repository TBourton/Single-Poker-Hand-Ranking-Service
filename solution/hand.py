from __future__ import annotations

from typing import Optional

import numpy as np
from card import Card, SuitT, ValueT
from pydantic import BaseModel, root_validator


class Hand(BaseModel):
    card0: Card
    card1: Card
    card2: Card
    card3: Card
    card4: Card

    @classmethod
    def from_string(cls, string: str, delimiter: str = " ") -> Hand:
        """Decode a hand from string of the format, e.g. "2H 3D 5S 9C KD"."""
        cards = string.split(delimiter)
        if len(cards) != 5:
            raise ValueError(
                f"Expected format '<v><s> <v><s> <v><s> <v><s>'"
                f" where <v> is card value 2,3,...,10,J,Q,K,A"
                f" and <s> is suit D,H,S,C. Got {string}"
            )

        return Hand(
            **{
                f"card{i}": Card.from_string(card)
                for i, card in enumerate(cards)
            }
        )

    @root_validator
    def all_cards_different(cls, values):
        cards = list(values.values())
        if any(c == cards[0] for c in cards[1:]):
            raise ValueError("some cards are the same!")
        return values

    def rank(self) -> str:
        """Rank this hand.

        Returns
        -------
        str
            Rank of the form '<rank_name>: <description>.

        """
        return (  # Note: call order matters.
            self._check_royal_flush()
            or self._check_straight_flush()
            or self._check_four_of_a_kind()
            or self._check_full_house()
            or self._check_flush()
            or self._check_straight()
            or self._check_three_of_a_kind()
            or self._check_two_pair()
            or self._check_pair()
            or self._check_high_card()
        )

    @property
    def cards(self) -> list[Card]:
        """Get the list of Card that make up this hand."""
        return [getattr(self, f"card{i}") for i in range(5)]

    @property
    def suits(self) -> set[SuitT]:
        """Get a set of the different suits in this hand."""
        return set(card.suit for card in self.cards)

    @property
    def values(self) -> list[ValueT]:
        """Get a list of values that make up this hand."""
        return sorted(card.value for card in self.cards)

    def _ns_value(self, n: int) -> Optional[ValueT]:
        """Get n's value, e.g. n=4 gives quad value, assumes unique."""
        values, counts = np.unique(self.values, return_counts=True)

        try:
            value = values[np.argwhere(counts == n)][0]
        except IndexError:
            return None

        return int(value)  # type: ignore

    @property
    def max_of_consecutive(self) -> Optional[ValueT]:
        values = self.values
        if len(set(values)) != 5:
            return None  # Values cannot be repeated

        if {14, 2, 3, 4, 5} == set(values):
            return 5

        if sorted(values) == list(range(min(values), max(values) + 1)):
            return max(values)

        return None

    def _check_royal_flush(self) -> Optional[str]:
        suits = self.suits
        if len(suits) != 1:
            return None

        values = set(self.values)
        if values != {14, 13, 12, 11, 10}:
            return None

        suit = suits.pop()
        return f"royal flush: {_format_suit(suit)}"

    def _check_straight_flush(self) -> Optional[str]:
        suits = self.suits
        if len(suits) != 1:
            return None

        max_value = self.max_of_consecutive
        if not max_value:
            return None

        suit = suits.pop()
        return (
            f"straight flush: {_format_value(max_value)}"
            f"-high {_format_suit(suit)}"
        )

    def _check_four_of_a_kind(self) -> Optional[str]:
        values, counts = np.unique(self.values, return_counts=True)

        quads_value = self._ns_value(4)
        if not quads_value:
            return None

        return f"four of a kind: {_format_value(quads_value)}"

    def _check_full_house(self) -> Optional[str]:
        trips_value = self._ns_value(3)
        pair_value = self._ns_value(2)
        if not pair_value or not trips_value:
            return None

        return (
            f"full house: {_format_value(trips_value)}"
            f" over {_format_value(pair_value)}"
        )

    def _check_flush(self) -> Optional[str]:
        suits = self.suits
        if len(suits) != 1:
            return None

        suit = suits.pop()
        return f"flush: {_format_suit(suit)}"

    def _check_straight(self) -> Optional[str]:
        max_consecutive_value = self.max_of_consecutive
        if not max_consecutive_value:
            return None

        return f"straight: {_format_value(max_consecutive_value)}-high"

    def _check_three_of_a_kind(self) -> Optional[str]:
        trips_value = self._ns_value(3)
        if not trips_value:
            return None

        return f"three of a kind: {_format_value(trips_value)}"

    def _check_two_pair(self) -> Optional[str]:
        values, counts = np.unique(self.values, return_counts=True)
        pairs = values[np.argwhere(counts == 2)].reshape(-1)
        if len(pairs) != 2:
            return None

        high = int(max(pairs))
        low = int(min(pairs))
        return f"two pair: {_format_value(high)} and {_format_value(low)}"

    def _check_pair(self) -> Optional[str]:
        values, counts = np.unique(self.values, return_counts=True)
        pair = self._ns_value(2)
        if not pair:
            return None

        return f"pair: {_format_value(pair)}"

    def _check_high_card(self) -> str:
        return f"high card: {_format_value(max(self.values))}"


def _format_suit(suit: SuitT) -> str:
    suit_map = {"S": "spades", "D": "diamonds", "H": "hearts", "C": "clubs"}
    return suit_map[suit]


def _format_value(value: ValueT) -> str:
    value_map = {i: str(i) for i in range(2, 11)} | {
        11: "Jack",
        12: "Queen",
        13: "King",
        14: "Ace",
    }
    return value_map[value]
