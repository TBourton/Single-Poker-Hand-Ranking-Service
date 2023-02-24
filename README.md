# Single Poker Hand Ranking Service (Giff Gaff takehome solution)

## Problem
The code in this repo does the following:
- Takes a hand of cards and identifies the ranking of the given hand.
- Expose this algorithm via an endpoint `/rank`, that accepts a valid poker hand and returns its ranking.
- Rank information is formatted as `<rank_name>: <description>`, see description format for each different rank below.
<br>

### Hand Ranking Rules

A poker hand consists of 5 cards dealt from a deck. A deck is composed of 52 cards ordered as `2 through 10`, `J` (*Jack*), `Q` (*Queen*), `K` (*King*), and `A` (*Ace*); and split across 4 suits: *♠ Spades* (black), *♦ Diamonds* (red), *♣ Clubs* (black), and *♥ Hearts* (red).

Poker hands are ranked by the following partial order from highest to lowest:

**1. Royal Flush**  ~ `[ A♥ K♥ Q♥ J♥ 10♥ ]`

The best hand possible, a royal flush consists of A, K, Q, J and 10, all of the same suit.

Description format: `<suit>`

**2. Straight Flush** ~ `[ 6♥ 7♥ 8♥ 9♥ 10♥ ]`

Also very rare, a straight flush consists of any straight that is all the same suit. Note Ace can act as value `1` to form a straight with values `2 3 4 5`.

Description format: `<highest_value>-high <suit>`

**3. Four of a Kind** ~ `[ A♥ A♣ A♦ A♠ K♥ ]`

Four of a kind, or 'quads', consists of four cards of equal value along with another card known as a side card.

Description format: `<quads value>`

**4. Full House** ~ `[ A♥ A♣ A♦ K♠ K♥ ]`

A full house consists of three cards of one value and two cards of another.

Description format: `<trips_value> over <pair_value>`

**5. FLush** ~ `[ K♣ 10♣ 8♣ 7♣ 5♣ ]`

A flush is a hand which has all cards of the same suit.

Description format: `<suit>`

**6. Straight** ~ `[ 10♥ 9♣ 8♦ 7♠ 6♥ ]`

A straight has five cards of consecutive value that are not all the same suit. Note Ace can act as value `1` to form a straight with values `2 3 4 5`.

Description format: `<highest_value>-high`

**7. Three of a Kind** ~ `[ A♥ A♣ A♦ K♠ Q♥ ]`

Also known as 'trips', three of a kind is 3 cards of the same value and 2 side cards of different values.

Description format: `<trips value>`

**8. Two Pair** ~ `[ A♥ A♣ K♦ K♠ 7♥ ]`

Two pair cosists of two sets of cards of the same value, and one extra card.

Description format: `<high_pair_value> and <low_pair_value>`

**9. Pair** ~ `[ A♥ A♣ K♦ J♠ 7♥ ]`

One pair consists of two cards of the same value, and three extra cards.

Description format: `<pair_value>`

**10. High Card** ~ `[ A♥ K♣ Q♦ 9♠ 7♥ ]`

Five cards that do not interact with each other to make any of the above hands.

Description format: `<value>`

<br>

### Samples:

```
Query: "2H 3D 5S 9C KD"
Result: "high card: King"

~

Query: "2H 4D 4S 2C 4H"
Result: "full house: 4 over 2"

~

Query: "6H 7H 8H 9H 10H"
Result: "straight flush: 10-high hearts"
```

# Installation instructions and explanation

The solution can be found in the `./solution` directory. It contains three modules (+ unit tests):
- app.py - defines the API endpoint
- hand.py - defines class for defining a hand made up of 5 cards + the logic for ranking the hand
- card.py - defines class for defining a card made up of a suit + card value


## Run the python module directly
Navigate to the correct directory `cd solution`. The python hand ranker module can be run directly:
```python
from hand import Hand

hand = Hand.from_string("2D 7H 9C 9H 9D")
hand.rank()
>>> "three of a kind: 9"
```


## Run the API via run script
A convenient example run script, `run.sh`, is provided in the top level of this repo.
This script
- Installs dependencies
- Brings up the API, served via uvicorn
- Runs some example querys (via calling query.py)
- Brings down the API.

Run it using
```sh
./run.sh
```

## Run the API standalone
To standup and run the API:
1. Install the requirements
```sh
python -m pip install -r requirements.txt
python -m pip install requests
```

2. In a seperate terminal (or background the app by using `&`). Bring up the app
```sh
cd solution
uvicorn app:app
```

3. Hit the app with a query. For example, using `curl`,
```sh
curl -X POST http://127.0.0.1:8000/rank -d '{"hand": "2D 7H 9C 9H 9D"}' -H 'Content-Type: application/json'
>>> "three of a kind: 9"
```

## Run the tests
To run the tests:
1. Install dependencies
```sh
pip install -r requirements.txt
pip install -r dev-requirements.txt
```
2. Run the test suite
```sh
cd solution
pytest tests
```

## Development

### Pre-commit hook
For development the pre-commit hook should be installed. To install it:
```sh
pip install pre-commit
pre-commit install
```
Update it with `pre-commit autoupdate`.

### Update dependencies
For simplicity, `pip-tools` is used for dependency management. To upgrade reqs files:
```sh
pip install pip-tools
pip-compile --no-emit-find-links --no-emit-index-url requirements.in -o requirements.txt
pip-compile --no-emit-find-links --no-emit-index-url dev-requirements.in -o dev-requirements.txt
```
