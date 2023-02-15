import pytest

from pydantic import ValidationError

from hand import ALLOWED_SUITS, ALLOWED_VALUES, Card, Hand, SuitT, ValueT


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


def test_hand_happy():
    card = Card(suit="H", value=2)
    assert Hand(
        card1=card,
        card2=card,
        card3=card,
        card4=card,
        card5=card,
    )
