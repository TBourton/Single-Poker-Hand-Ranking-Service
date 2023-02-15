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
    with pytest.raises(ValidationError):
        Hand(**{f"card{i}": 7 for i in range(5)})


def test_hand_all_same_cards():
    card = Card(suit="H", value=2)
    with pytest.raises(ValidationError):
        assert Hand(**{f"card{i}": card for i in range(5)})


def test_hand_from_string_unhappy():
    with pytest.raises(ValueError):
        Hand.from_string("foo")


def test_hand_from_string_happy():
    assert Hand.from_string("2H 3D 5S 9C KD")


def test_card_eq():
    assert Card(suit="D", value=4) == Card(suit="D", value=4)


def test_card_neq():
    assert Card(suit="D", value=4) != Card(suit="D", value=7)
