import pytest

from pydantic import ValidationError

from hand import ALLOWED_SUITS, ALLOWED_VALUES, Card, Hand, SuitT, ValueT


@pytest.mark.parametrize("suit", ALLOWED_SUITS)
@pytest.mark.parametrize("value", ALLOWED_VALUES)
def test_card_happy(suit: SuitT, value: ValueT):
    assert Card(suit=suit, value=value)


@pytest.mark.parametrize("suit", ["foo", 1])
@pytest.mark.parametrize("value", ["bar", 7])
def test_card_unhappy(suit, value):
    with pytest.raises(ValidationError):
        Card(suit=suit, value=value)


def test_hand_happy():
    card = Card(suit="H", value=2)
    assert Hand(
        card1=card,
        card2=card,
        card3=card,
        card4=card,
        card5=card,
    )


def test_hand_unhappy():
    card = Card(suit="H", value=2)
    with pytest.raises(ValidationError):
        Hand(
            card1=7,
            card2=card,
            card3=card,
            card4=card,
            card5=card,
        )
