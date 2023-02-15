import pytest

from hand import Hand

# rank_name, description, hand
TEST_CASES = [
    ("royal flush", "hearts", "AH KH QH JH 10H"),
    ("straight flush", "A-high hearts", "10H JH QH KH AH"),  # with ace high
    ("straight flush", "5-high diamonds", "AD 2D 3D 4D 5D"),  # with ace low
    ("four of a kind", "Q", "QH QD QC QS 10H"),
    ("full house", "A over K", "AH AD AC KH KS"),
    ("flush", "S", "KS 2S 3S QS 7S"),
    ("straight", "A-high", "10C JH QC KS AH"),  # with ace high
    ("straight", "5-high", "AC 2H 3S 4S 5H"),  # with ace low
    ("three of a kind", "A", "AH AC AS QS QH"),
    ("two-pair", "A and K", "AH AC KS KS QH"),
    ("pair", "A", "AH AC KD JS 7H"),
    ("high card", "A", "AH KC QD 9S 7H"),
]


@pytest.mark.parametrize("rank_name,desc,hand_str", TEST_CASES)
def test_ranker(rank_name: str, desc: str, hand_str: str):
    hand = Hand.from_string(hand_str)
    expected_out = f"{rank_name}: {desc}"
    assert hand.rank() == expected_out
