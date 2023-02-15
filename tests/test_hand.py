import pytest

from pydantic import ValidationError

from hand import ALLOWED_SUITS, ALLOWED_VALUES, Card, SuitT, ValueT


@pytest.mark.parametrize("suit", ALLOWED_SUITS)
@pytest.mark.parametrize("value", ALLOWED_VALUES)
def test_card(suit: SuitT, value: ValueT):
    print(suit, value)
    print(help(Card))
    _ = Card(suit=suit, value=value)


@pytest.mark.parametrize("suit", ["foo", 1])
@pytest.mark.parametrize("value", ["bar", 7])
def test_card_fail(suit, value):
    with pytest.raises(ValidationError):
        Card(suit=suit, value=value)
