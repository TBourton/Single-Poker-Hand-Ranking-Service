from typing import get_args

import pytest

from card import Card, SuitT, ValueT
from pydantic import ValidationError

ALLOWED_SUITS = set(get_args(SuitT))
ALLOWED_VALUES = set(get_args(ValueT))


@pytest.mark.parametrize("suit", ALLOWED_SUITS)
@pytest.mark.parametrize("value", ALLOWED_VALUES)
def test_card_happy(suit: SuitT, value: ValueT):
    assert Card(suit=suit, value=value)


@pytest.mark.parametrize("suit", ["foo", 2, 7])
@pytest.mark.parametrize("value", ["bar", "H", 1])
def test_card_unhappy(suit, value):
    with pytest.raises(ValidationError):
        Card(suit=suit, value=value)


@pytest.mark.parametrize("suit", ALLOWED_SUITS)
@pytest.mark.parametrize("value", ALLOWED_VALUES)
def test_card_from_string_happy(suit: SuitT, value: ValueT):
    string = f"{value}{suit}"
    assert Card.from_string(string)


@pytest.mark.parametrize("suit", ["foo", 2, 7])
@pytest.mark.parametrize("value", ["bar", "H", 1])
def test_card_from_string_unhappy(suit, value):
    string = f"{value}{suit}"
    with pytest.raises(ValidationError):
        Card.from_string(string)


def test_card_eq():
    assert Card(suit="D", value=4) == Card(suit="D", value=4)


def test_card_neq():
    assert Card(suit="D", value=4) != Card(suit="D", value=7)
