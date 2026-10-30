#!/usr/bin/env python3
"""Scan a Zeek http.log (default TSV format) for common web attack patterns."""
import re
import sys
from collections import Counter
from urllib.parse import unquote

PATTERNS = {
    "SQL Injection": re.compile(r"(union\s+select|'\s*or\s*'?\d+'?\s*=\s*'?\d+|'\s*--|sleep\(\d+\))", re.I),
    "XSS": re.compile(r"(<script|onerror\s*=|onload\s*=|javascript:)", re.I),
    "Path Traversal": re.compile(r"(\.\./|\.\.\\)"),
}
SCANNER_UA = re.compile(r"(nikto|sqlmap|gobuster|nmap|dirbuster)", re.I)


def read_zeek_log(path):
    fields = []
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith("#fields"):
                fields = line.split("\t")[1:]
            elif line and not line.startswith("#"):
                yield dict(zip(fields, line.split("\t")))


def main(path):
    alerts = Counter()
    for rec in read_zeek_log(path):
        uri = unquote(unquote(rec.get("uri", "")))
        src = rec.get("id.orig_h", "?")
        for name, rx in PATTERNS.items():
            if rx.search(uri):
                alerts[name] += 1
                print(f"[ALERT] {name:15} src={src} uri={uri[:100]}")
        if SCANNER_UA.search(rec.get("user_agent", "")):
            alerts["Scanner UA"] += 1
            print(f"[ALERT] Scanner UA      src={src} ua={rec['user_agent'][:60]}")

    print("\n=== Summary ===")
    if not alerts:
        print("No attack patterns detected.")
    for name, count in alerts.most_common():
        print(f"{name}: {count}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "http.log")
