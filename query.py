#!/bin/python3
import requests


def main(address: str = "http://127.0.0.1:8000"):
    assert requests.get(f"{address}/docs").status_code == 200

    test_hands = ["2H 3D 5S 9C KD", "2H 4D 4S 2C 4H", "6H 7H 8H 9H 10H"]
    for hand in test_hands:
        print(f"Query: {hand}")
        resp = requests.post(f"{address}/rank", json={"hand": hand})
        assert resp.status_code == 200
        print(f"Result: {resp.text}")
        print("~~~~~~~~~~~~~~~~~~~~~\n")


if __name__ == "__main__":
    main()
