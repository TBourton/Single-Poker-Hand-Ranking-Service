from __future__ import annotations

from typing import Literal, Optional, get_args

import numpy as np
from pydantic import BaseModel, root_validator

SuitT = Literal["S", "D", "H", "C"]
ValueT = Literal[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
ALLOWED_SUITS = set(get_args(SuitT))
ALLOWED_VALUES = set(get_args(ValueT))

VALUE_MAP = {i: i for i in range(2, 11)} | {11: "J", 12: "Q", 13: "K", 14: "A"}
VALUE_MAP_INV = {v: k for k, v in VALUE_MAP.items()}
SUIT_FORMAT_MAP = {"S": "spades", "D": "diamonds", "H": "hearts", "C": "clubs"}
VALUE_FORMAT_MAP = {i: i for i in range(2, 11)} | {
    11: "Jack",
    12: "Queen",
    13: "King",
    14: "Ace",
}


class Card(BaseModel):
    suit: SuitT
    value: ValueT

    @classmethod
    def from_string(cls, string: str) -> Card:
        """Decode a card from string of the format <value><suit>."""
        suit = string[-1]  # Suit is max 1 char
        value = string[:-1]  # And value is the rest
        try:
            value = int(value)
        except ValueError:
            value = VALUE_MAP_INV.get(value)

        return Card(suit=suit, value=value)  # type: ignore


class Hand(BaseModel):
    card0: Card
    card1: Card
    card2: Card
    card3: Card
    card4: Card

    @classmethod
    def from_string(cls, string: str, delimiter: str = " ") -> Hand:
        """Decode a card from string of the format, e.g. "2H 3D 5S 9C KD"."""
        cards = string.split(delimiter)
        print(cards)
        if len(cards) != 5:
            raise ValueError(f"Expected format '2H 3D 5S 9C KD', got {string}")

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
        return (
            self._check_royal_flush()
            or self._check_straight_flush()
            or self._check_four_of_a_kind()
            or self._check_full_house()
            or self._check_flush()
        )

    @property
    def cards(self) -> list[Card]:
        return [getattr(self, f"card{i}") for i in range(5)]

    @property
    def suits(self) -> list[SuitT]:
        return [card.suit for card in self.cards]

    @property
    def values(self) -> list[ValueT]:
        return [card.value for card in self.cards]

    @property
    def min_value(self) -> ValueT:
        return min(self.values)

    @property
    def max_value(self) -> ValueT:
        return max(self.values)

    def _ns_value(self, n: int) -> Optional[ValueT]:
        """Get n's value, e.g. n=4 gives quad value."""
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
        suits = set(self.suits)
        if len(suits) != 1:
            return None

        values = set(self.values)
        if values != {14, 13, 12, 11, 10}:
            return None

        suit = suits.pop()
        return f"royal flush: {SUIT_FORMAT_MAP[suit]}"

    def _check_straight_flush(self) -> Optional[str]:
        suits = set(self.suits)
        if len(suits) != 1:
            return None

        max_value = self.max_of_consecutive
        if not max_value:
            return None

        suit = suits.pop()
        return (
            f"straight flush: {VALUE_FORMAT_MAP[max_value]}"
            f"-high {SUIT_FORMAT_MAP[suit]}"
        )

    def _check_four_of_a_kind(self) -> Optional[str]:
        values, counts = np.unique(self.values, return_counts=True)

        quads_value = self._ns_value(4)
        if not quads_value:
            return None

        return f"four of a kind: {VALUE_FORMAT_MAP[quads_value]}"

    def _check_full_house(self) -> Optional[str]:
        trips_value = self._ns_value(3)
        pair_value = self._ns_value(2)
        if not pair_value or not trips_value:
            return None

        return (
            f"full house: {VALUE_FORMAT_MAP[trips_value]}"
            f" over {VALUE_FORMAT_MAP[pair_value]}"
        )

    def _check_flush(self) -> Optional[str]:
        suits = set(self.suits)
        if len(suits) != 1:
            return None

        suit = suits.pop()
        return f"flush: {SUIT_FORMAT_MAP[suit]}"
