from __future__ import annotations

from typing import Literal, get_args

from pydantic import BaseModel

SuitT = Literal["S", "D", "H", "C"]
ValueT = Literal[2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
ALLOWED_SUITS = set(get_args(SuitT))
ALLOWED_VALUES = set(get_args(ValueT))


class Card(BaseModel):
    suit: SuitT
    value: ValueT

    @classmethod
    def from_string(cls, string: str) -> Card:
        """Decode a card from string of the format <value><suit>."""
        print(string)
        suit = string[-1]  # Suit is max 1 char
        value = string[:-1]  # And value is the rest
        try:
            value = int(value)
        except ValueError:
            pass

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
