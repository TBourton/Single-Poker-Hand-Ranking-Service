from typing import Literal, get_args

from pydantic import BaseModel

SuitT = Literal["S", "D", "H", "C"]
ValueT = Literal[2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
ALLOWED_SUITS = set(get_args(SuitT))
ALLOWED_VALUES = set(get_args(ValueT))


class Card(BaseModel):
    suit: SuitT
    value: ValueT


class Hand(BaseModel):
    card1: Card
    card2: Card
    card3: Card
    card4: Card
    card5: Card
