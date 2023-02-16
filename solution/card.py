from __future__ import annotations

from typing import Literal

from pydantic import BaseModel

SuitT = Literal["S", "D", "H", "C"]
ValueT = Literal[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


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
            _map = {"J": 11, "Q": 12, "K": 13, "A": 14}
            value = _map.get(value)

        return Card(suit=suit, value=value)  # type: ignore
