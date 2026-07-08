#!/usr/bin/env python3
"""Validate a JSON monitoring-target allowlist."""

import argparse
import ipaddress
import json
import re
from pathlib import Path
from urllib.parse import urlsplit


ALLOWED_CHECKS = {"dns", "http", "tls", "ping", "traceroute", "tcp"}
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SENSITIVE_KEYS = {"token", "key", "password", "secret", "authorization", "cookie"}


def public_ip(value):
    try:
        address = ipaddress.ip_address(value)
    except ValueError:
        return True
    return address.is_global


def validate_target(item, index):
    errors = []
    prefix = "targets[%d]" % index
    if not isinstance(item, dict):
        return [prefix + " must be an object"]
    target_id = item.get("id")
    if not isinstance(target_id, str) or not ID_PATTERN.match(target_id):
        errors.append(prefix + ".id must be unique hyphen-case")
    if not isinstance(item.get("enabled"), bool):
        errors.append(prefix + ".enabled must be boolean")
    target = item.get("target")
    if not isinstance(target, str) or not target:
        errors.append(prefix + ".target is required")
        return errors
    if "*" in target or "/" in target and not target.startswith(("http://", "https://")):
        errors.append(prefix + ".target must not be a wildcard or CIDR")
    parsed = urlsplit(target if "://" in target else "//" + target)
    if parsed.scheme and parsed.scheme not in {"http", "https"}:
        errors.append(prefix + ".target URL scheme must be http or https")
    if parsed.username or parsed.password:
        errors.append(prefix + ".target must not contain credentials")
    host = parsed.hostname
    if not host:
        errors.append(prefix + ".target must contain a hostname or public IP")
    elif host.lower() in {"localhost", "metadata.google.internal"} or not public_ip(host):
        errors.append(prefix + ".target must not be local, private, or special-use")
    query = parsed.query.lower()
    if any(key in query for key in SENSITIVE_KEYS):
        errors.append(prefix + ".target query appears to contain sensitive data")
    checks = item.get("checks")
    if not isinstance(checks, list) or not checks:
        errors.append(prefix + ".checks must be a non-empty list")
    else:
        unknown = sorted(set(checks) - ALLOWED_CHECKS)
        if unknown:
            errors.append(prefix + ".checks contains unsupported values: " + ", ".join(unknown))
    try:
        parsed_port = parsed.port
    except ValueError:
        parsed_port = None
        errors.append(prefix + ".target contains an invalid port")
    if "tcp" in (checks or []) and not parsed_port and not isinstance(item.get("port"), int):
        errors.append(prefix + ".port is required for TCP hostname/IP checks")
    port = item.get("port")
    if port is not None and (not isinstance(port, int) or not 1 <= port <= 65535):
        errors.append(prefix + ".port must be an integer from 1 to 65535")
    if not isinstance(item.get("owner"), str) or not item.get("owner", "").strip():
        errors.append(prefix + ".owner is required")
    return errors


def validate(document):
    errors = []
    if not isinstance(document, dict):
        return ["document must be an object"]
    if document.get("version") != 1:
        errors.append("version must equal 1")
    targets = document.get("targets")
    if not isinstance(targets, list):
        return errors + ["targets must be a list"]
    seen = set()
    seen_scopes = set()
    for index, item in enumerate(targets):
        errors.extend(validate_target(item, index))
        if isinstance(item, dict) and isinstance(item.get("id"), str):
            if item["id"] in seen:
                errors.append("duplicate target id: " + item["id"])
            seen.add(item["id"])
        if isinstance(item, dict) and isinstance(item.get("target"), str):
            raw_target = item["target"]
            parsed = urlsplit(raw_target if "://" in raw_target else "//" + raw_target)
            try:
                parsed_port = parsed.port
            except ValueError:
                parsed_port = None
            scope = (
                parsed.scheme.lower(),
                (parsed.hostname or "").lower(),
                parsed_port or item.get("port"),
                parsed.path or "/",
                tuple(sorted(item.get("checks", []))) if isinstance(item.get("checks"), list) else (),
            )
            if scope in seen_scopes:
                errors.append("duplicate monitoring scope at targets[%d]" % index)
            seen_scopes.add(scope)
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target_file")
    args = parser.parse_args()
    document = json.loads(Path(args.target_file).read_text(encoding="utf-8"))
    errors = validate(document)
    if errors:
        for error in errors:
            print("ERROR: " + error)
        raise SystemExit(1)
    print("Target list is valid: %d target(s)" % len(document["targets"]))


if __name__ == "__main__":
    main()
