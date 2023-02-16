# Giff Gaff - Solution to hand ranker.

Developed on Python 3.9. Tests could be expanded in the future to test other py version, e.g. by using tox.

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
uvicorn app:app
```

3. Hit the app with a query. For example, using `curl`,
```sh
curl -X POST http://127.0.0.1:8000/rank -d '{"hand": "2D 7H 9C 9H 9D"}' -H 'Content-Type: application/json'
>>> "three of a kind: 9"
```

## Run the tests:
To run the tests:
1. Install dependencies
```sh
pip install -r requirements.txt
pip install -r dev-requirements.txt
```
2. Run the test suite
```sh
pytest tests
```

## Development

### Pre-commit hook
For development, I am using pre-commit. To install it:
```sh
pip install pre-commit
pre-commit install
```
Update it with `pre-commit autoupdate`.

### Update dependencies
For simplicity, I am using `pip-tools`. To upgrade reqs files:

```sh
pip install pip-tools
pip-compile --no-emit-find-links --no-emit-index-url requirements.in -o requirements.txt
pip-compile --no-emit-find-links --no-emit-index-url dev-requirements.in -o dev-requirements.txt
```