#!/usr/bin/env python3
"""Compare two normalized infrastructure snapshots and emit a JSON diff."""

import argparse
import json
from pathlib import Path


SEVERITY = {
    "unknown": 0,
    "info": 1,
    "ok": 1,
    "low": 2,
    "warning": 3,
    "warn": 3,
    "high": 4,
    "critical": 5,
}


def load(path):
    with Path(path).open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict) or not isinstance(value.get("systems"), dict):
        raise ValueError("snapshot must be an object containing a systems object")
    return value


def flatten(snapshot):
    entities = {}
    completeness = {}
    for system, payload in snapshot["systems"].items():
        if not isinstance(payload, dict):
            raise ValueError("system payload must be an object: %s" % system)
        completeness[system] = bool(payload.get("complete", False))
        for entity in payload.get("entities", []):
            if not isinstance(entity, dict):
                raise ValueError("entity must be an object in system: %s" % system)
            kind = str(entity.get("kind", "unknown"))
            entity_id = entity.get("id")
            if entity_id is None or str(entity_id) == "":
                raise ValueError("entity id is required in system: %s" % system)
            key = (system, kind, str(entity_id))
            if key in entities:
                raise ValueError("duplicate entity key: %s/%s/%s" % key)
            entities[key] = entity
    return entities, completeness


def record(key, entity):
    system, kind, entity_id = key
    return {
        "system": system,
        "kind": kind,
        "id": entity_id,
        "name": entity.get("name"),
        "status": entity.get("status"),
        "severity": entity.get("severity", "unknown"),
    }


def rank(entity):
    return SEVERITY.get(str(entity.get("severity", "unknown")).lower(), 0)


def compare(before, after):
    old, old_complete = flatten(before)
    new, new_complete = flatten(after)
    result = {
        "baseline_observed_at": before.get("observed_at"),
        "current_observed_at": after.get("observed_at"),
        "added": [],
        "removed": [],
        "regressed": [],
        "recovered": [],
        "changed": [],
        "suppressed_removals": [],
    }

    for key in sorted(new.keys() - old.keys()):
        result["added"].append(record(key, new[key]))

    for key in sorted(old.keys() - new.keys()):
        item = record(key, old[key])
        system = key[0]
        if old_complete.get(system, False) and new_complete.get(system, False):
            result["removed"].append(item)
        else:
            item["reason"] = "source snapshots are not both complete"
            result["suppressed_removals"].append(item)

    for key in sorted(old.keys() & new.keys()):
        left, right = old[key], new[key]
        if left == right:
            continue
        item = record(key, right)
        item["previous_status"] = left.get("status")
        item["previous_severity"] = left.get("severity", "unknown")
        item["attributes_changed"] = left.get("attributes", {}) != right.get("attributes", {})
        if rank(right) > rank(left):
            result["regressed"].append(item)
        elif rank(right) < rank(left):
            result["recovered"].append(item)
        else:
            result["changed"].append(item)

    result["summary"] = {name: len(items) for name, items in result.items() if isinstance(items, list)}
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("baseline", help="baseline snapshot JSON")
    parser.add_argument("current", help="current snapshot JSON")
    parser.add_argument("--output", help="write the diff to this file instead of stdout")
    args = parser.parse_args()
    result = compare(load(args.baseline), load(args.current))
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
