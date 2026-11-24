"""Replay the answer key against the running Pelita Ideas service.

Usage:
    python check_ideas.py                       # Feature 1: submit and browse (sample-data/ideas-scenario.csv)
    python check_ideas.py --feature 2           # Feature 2: vote and rank   (sample-data/votes-scenario.csv)
    python check_ideas.py --base-url http://localhost:9000

Standard library only. Every run tags its idea titles with a fresh run code, so
you can run it as often as you like against the same server. If the rankings
look crowded after many runs, restart the service.
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

DATA = Path(__file__).parent / "sample-data"
UTC_TIME = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z$")
IDEA_FIELDS = ("idea_id", "title", "description", "category", "submitted_by",
               "submitter_name", "department", "submitted_at", "vote_count")
FILLER = "Let drivers swap shifts in the app so that every route is always covered "


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


def load(name):
    return list(csv.DictReader((DATA / name).open(encoding="utf-8")))


STAFF = {row["staff_id"]: row for row in load("staff.csv")}


def make_title(raw, tag):
    """Tag a scenario title with the run code. '<N>' means: a title exactly N characters long."""
    m = re.fullmatch(r"<(\d+)>", raw.strip())
    if m:
        n = int(m.group(1))
        core = (FILLER * 3)[: n - len(tag) - 1].rstrip()
        core = core + "." * (n - len(tag) - 1 - len(core))
        return f"{tag} {core}"
    if not raw.strip():
        return raw
    lead = raw[: len(raw) - len(raw.lstrip())]
    trail = raw[len(raw.rstrip()):]
    return f"{lead}{tag} {raw.strip()}{trail}"


def check_idea(idea):
    """Return a list of problems with an idea body."""
    if not isinstance(idea, dict):
        return ["response body is not a JSON object"]
    problems = [f"missing field '{f}'" for f in IDEA_FIELDS if f not in idea]
    if problems:
        return problems
    staff = STAFF.get(idea["submitted_by"])
    if staff is None:
        problems.append(f"submitted_by {idea['submitted_by']!r} is not in staff.csv")
    else:
        if idea["submitter_name"] != staff["name"]:
            problems.append(f"submitter_name is {idea['submitter_name']!r}, expected {staff['name']!r}")
        if idea["department"] != staff["department"]:
            problems.append(f"department is {idea['department']!r}, expected {staff['department']!r}")
    if not isinstance(idea["submitted_at"], str) or not UTC_TIME.match(idea["submitted_at"]):
        problems.append(f"submitted_at {idea['submitted_at']!r} is not UTC ISO 8601 ending in Z")
    if not isinstance(idea["vote_count"], int):
        problems.append(f"vote_count {idea['vote_count']!r} is not a whole number")
    return problems


def run_ideas(list_ideas, tag):
    """Return the ideas from this run, in the order the list endpoint gave them."""
    status, body = list_ideas()
    if status != 200 or not isinstance(body, dict) or not isinstance(body.get("ideas"), list):
        return None, [f"list returned status {status} without an 'ideas' list"]
    return [i for i in body["ideas"] if isinstance(i, dict) and tag in str(i.get("title", ""))], []


def feature_1(base, tag):
    rows = load("ideas-scenario.csv")
    ids, titles = {}, {}
    drift, extra = 0, set()  # earlier wrong answers, so one mistake fails only its own step
    list_ideas = lambda: call("GET", f"{base}/ideas")
    passed = 0
    for row in rows:
        step, problems = row["step"], []
        expected_status = int(row["expected_status"])
        if row["action"] == "submit":
            title = make_title(row["title"], tag)
            body = {"title": title, "description": f"Workshop check run {tag}, step {step}",
                    "category": row["category"], "submitted_by": row["submitted_by"]}
            status, payload = call("POST", f"{base}/ideas", body)
            label = f"submit '{row['title'].strip()[:24] or '(blank)'}'"
            if status == expected_status == 201:
                problems += check_idea(payload)
                if isinstance(payload, dict):
                    ids[step], titles[step] = payload.get("idea_id"), title
                    if payload.get("title") != title:
                        problems.append("the title was changed: it must be stored exactly as typed")
                    if payload.get("vote_count") != 0:
                        problems.append(f"vote_count is {payload.get('vote_count')!r} on a new idea, expected 0")
        elif row["action"] == "list":
            status, payload = list_ideas()
            label = "list ideas"
        else:
            idea_id = ids.get(row["ref"], f"IDEA-NOT-REAL-{tag[1:]}")
            status, payload = call("GET", f"{base}/ideas/{idea_id}")
            label = f"get idea from step {row['ref']}" if row["ref"] in ids else "get an unknown idea"
            if status == expected_status == 200:
                problems += check_idea(payload)
                if isinstance(payload, dict) and payload.get("title") != titles.get(row["ref"]):
                    problems.append("title does not match what was submitted")

        if status != expected_status:
            problems.append(f"status {status}, expected {expected_status}")
            if row["action"] == "submit" and status == 201:
                drift += 1
                if isinstance(payload, dict):
                    extra.add(payload.get("idea_id"))
            elif row["action"] == "submit" and expected_status == 201:
                drift -= 1

        # Whatever the request did, the list must now be in the expected state
        # (allowing for earlier steps that already failed).
        mine, errs = run_ideas(list_ideas, tag)
        problems += errs
        if mine is not None:
            if row["expected_count"] and len(mine) != int(row["expected_count"]) + drift:
                problems.append(f"{len(mine)} ideas from this run in the list, expected {int(row['expected_count']) + drift}")
            if row["expected_order"]:
                want = [ids[s] for s in row["expected_order"].split("|") if s in ids]
                got = [i.get("idea_id") for i in mine if i.get("idea_id") not in extra]
                if got != want:
                    problems.append(f"order is {got}, expected newest first {want}")
            for idea in mine:
                problems += [f"in the list: {p}" for p in check_idea(idea)]

        passed += report(step, label, row["what_happens"], problems)
    return passed, len(rows)


SETUP = [("A", "Weekly route review with drivers", "Process", "E1001"),
         ("B", "Reusable parcel bags", "Sustainability", "E1002"),
         ("C", "Night-shift safety vests", "Safety", "E1006"),
         ("D", "Swap shifts in the app", "Process", "E1004")]


def feature_2(base, tag):
    ids = {}
    for key, title, category, who in SETUP:
        status, payload = call("POST", f"{base}/ideas", {"title": f"{tag} {title}", "category": category,
                                                         "description": f"Vote check {tag}", "submitted_by": who})
        if status != 201 or not isinstance(payload, dict):
            print(f"Setup failed: submitting idea {key} returned {status}. Make Feature 1 pass first.")
            return 0, 1
        ids[key] = payload["idea_id"]
    names = {v: k for k, v in ids.items()}

    rows = load("votes-scenario.csv")
    passed = 0
    for row in rows:
        step, problems = row["step"], []
        expected_status = int(row["expected_status"])
        if row["action"] == "vote":
            idea_id = ids.get(row["idea"], f"IDEA-NOT-REAL-{tag[1:]}")
            status, payload = call("POST", f"{base}/ideas/{idea_id}/votes", {"voter": row["voter"]})
            label = f"{row['voter']} votes for idea {row['idea']}"
            if status == expected_status == 201:
                problems += check_idea(payload)
            if row["expected_votes"]:
                s, idea = call("GET", f"{base}/ideas/{idea_id}")
                got = idea.get("vote_count") if isinstance(idea, dict) else None
                if got != int(row["expected_votes"]):
                    problems.append(f"idea {row['idea']} has vote_count {got!r}, expected {row['expected_votes']}")
        else:
            limit = int(row["limit"])
            status, payload = call("GET", f"{base}/rankings?limit={limit}")
            label = f"rankings, limit {limit}"
            if status == expected_status == 200:
                ideas = payload.get("ideas") if isinstance(payload, dict) else None
                if not isinstance(ideas, list):
                    problems.append("no 'ideas' list in the rankings")
                else:
                    if len(ideas) > limit:
                        problems.append(f"{len(ideas)} ideas returned for limit {limit}")
                    votes = [i.get("vote_count", 0) for i in ideas]
                    if votes != sorted(votes, reverse=True):
                        problems.append(f"not sorted by votes: {votes}")
                    if row["expected_order"]:
                        got = [names[i["idea_id"]] for i in ideas if i.get("idea_id") in names]
                        want = row["expected_order"].split("|")
                        if got != want:
                            problems.append(f"order of this run's ideas is {got}, expected {want}")
        if status != expected_status:
            problems.append(f"status {status}, expected {expected_status}")
        passed += report(step, label, row["what_happens"], problems)
    return passed, len(rows)


def report(step, label, what, problems):
    mark = "PASS" if not problems else "FAIL"
    print(f"{mark}  step {step:>2}  {label:<36} ({what})")
    for p in dict.fromkeys(problems):
        print(f"          - {p}")
    return not problems


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--base-url", default="http://127.0.0.1:8000")
    parser.add_argument("--feature", type=int, choices=(1, 2), default=1)
    args = parser.parse_args()
    base = args.base_url.rstrip("/")
    tag = "#" + uuid.uuid4().hex[:6]

    try:
        call("GET", f"{base}/ideas")
    except urllib.error.URLError as err:
        print(f"Cannot reach {base}: {err.reason}. Is the service running?")
        return 2

    passed, total = (feature_1 if args.feature == 1 else feature_2)(base, tag)
    print(f"\n{passed}/{total} steps match the answer key (Feature {args.feature}).")
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
