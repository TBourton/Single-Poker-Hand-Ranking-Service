import pytest

from card import Card
from hand import Hand
from pydantic import ValidationError


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
