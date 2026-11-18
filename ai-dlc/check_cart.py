"""Replay sample-data/cart-scenario.csv against the running cart service.

Usage:
    python check_cart.py                          # http://localhost:8000
    python check_cart.py --base-url http://localhost:9000

Standard library only. Each run uses fresh cart ids, so you can run it as often
as you like against the same server.
"""

import argparse
import csv
import json
import re
import sys
import urllib.error
import urllib.request
import uuid
from pathlib import Path

SCENARIO = Path(__file__).parent / "sample-data" / "cart-scenario.csv"
MONEY = re.compile(r"^-?\d+\.\d{2}$")


def call(method, url, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status, _json(resp.read())
    except urllib.error.HTTPError as err:
        return err.code, _json(err.read())


def _json(raw):
    try:
        return json.loads(raw or b"null")
    except ValueError:
        return None


def check_cart_body(cart, expected_count, expected_subtotal):
    """Return a list of problems with a cart body."""
    if not isinstance(cart, dict):
        return ["response body is not a JSON object"]
    problems = []
    for field in ("cart_id", "lines", "item_count", "subtotal"):
        if field not in cart:
            problems.append(f"missing field '{field}'")
    if problems:
        return problems
    if cart["item_count"] != int(expected_count):
        problems.append(f"item_count is {cart['item_count']!r}, expected {int(expected_count)}")
    subtotal = cart["subtotal"]
    if not isinstance(subtotal, str) or not MONEY.match(subtotal):
        problems.append(f"subtotal {subtotal!r} is not a string with 2 decimals")
    elif subtotal != expected_subtotal:
        problems.append(f"subtotal is {subtotal}, expected {expected_subtotal}")
    seen = set()
    for line in cart["lines"]:
        pid = line.get("product_id")
        if pid in seen:
            problems.append(f"product {pid} appears on more than one line")
        seen.add(pid)
        for money_field in ("unit_price", "line_total"):
            value = line.get(money_field)
            if not isinstance(value, str) or not MONEY.match(value):
                problems.append(f"{pid}: {money_field} {value!r} is not a string with 2 decimals")
        if not line.get("name"):
            problems.append(f"{pid}: missing product name")
    return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--base-url", default="http://localhost:8000")
    args = parser.parse_args()
    base = args.base_url.rstrip("/")

    run = uuid.uuid4().hex[:6]
    rows = list(csv.DictReader(SCENARIO.open(encoding="utf-8")))
    passed = 0

    try:
        call("GET", f"{base}/carts/ping-{run}")
    except urllib.error.URLError as err:
        print(f"Cannot reach {base}: {err.reason}. Is the service running?")
        return 2

    for row in rows:
        cart_id = f"{row['cart']}-{run}"
        cart_url = f"{base}/carts/{cart_id}"
        if row["action"] == "add":
            body = {"product_id": row["product_id"], "quantity": int(row["quantity"])}
            status, payload = call("POST", f"{cart_url}/items", body)
            label = f"add {row['quantity']} x {row['product_id']} to cart {row['cart']}"
        else:
            status, payload = call("GET", cart_url)
            label = f"get cart {row['cart']}"

        problems = []
        expected_status = int(row["expected_status"])
        if status != expected_status:
            problems.append(f"status {status}, expected {expected_status}")

        if row["expected_item_count"]:
            # Whatever the request did, the cart must now be in the expected state.
            if status in (200, 201) and status == expected_status:
                cart = payload
            else:
                _, cart = call("GET", cart_url)
            problems += check_cart_body(cart, row["expected_item_count"], row["expected_subtotal"])

        mark = "PASS" if not problems else "FAIL"
        print(f"{mark}  step {row['step']:>2}  {label:<36} ({row['what_happens']})")
        for problem in problems:
            print(f"          - {problem}")
        passed += not problems

    print(f"\n{passed}/{len(rows)} steps match the answer key.")
    return 0 if passed == len(rows) else 1


if __name__ == "__main__":
    sys.exit(main())
