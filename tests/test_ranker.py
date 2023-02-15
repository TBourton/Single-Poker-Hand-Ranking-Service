import pytest

from hand import Hand

# rank_name, description, hand
TEST_CASES = [
    (
        "royal flush",
        "hearts",
        "AH KH QH JH 10H",
    ),  # same as straight flush with ace high
    ("straight flush", "King-high hearts", "10H JH QH KH 9H"),
    ("straight flush", "5-high diamonds", "AD 2D 3D 4D 5D"),  # with ace low
    ("four of a kind", "Queen", "QH QD QC QS 10H"),
    ("full house", "Ace over King", "AH AD AC KH KS"),
    ("flush", "S", "KS 2S 3S QS 7S"),
    ("straight", "Ace-high", "10C JH QC KS AH"),  # with ace high
    ("straight", "5-high", "AC 2H 3S 4S 5H"),  # with ace low
    ("three of a kind", "Ace", "AH AC AS QS QH"),
    ("two-pair", "Ace and King", "AH AC KS KS QH"),
    ("pair", "Ace", "AH AC KD JS 7H"),
    ("high card", "Ace", "AH KC QD 9S 7H"),
]


@pytest.mark.parametrize("rank_name,desc,hand_str", TEST_CASES)
def test_ranker(rank_name: str, desc: str, hand_str: str):
    hand = Hand.from_string(hand_str)
    expected_out = f"{rank_name}: {desc}"
    assert hand.rank() == expected_out
