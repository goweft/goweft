#!/usr/bin/env python3
"""Profile CI: validate SVG assets and README links. Stdlib only."""

import pathlib
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent.parent
UA = {"User-Agent": "goweft-profile-ci/1.0 (+https://github.com/goweft/goweft)"}
SOFT_STATUS = {403, 405, 429}  # bot-hostile but not broken
TIMEOUT = 10

failures: list[str] = []
warnings: list[str] = []


def check_svgs() -> None:
    for svg in sorted(ROOT.glob("*.svg")):
        try:
            ET.parse(svg)
            print(f"  ok   {svg.name}")
        except ET.ParseError as exc:
            failures.append(f"{svg.name}: XML parse error: {exc}")


def readme_urls_and_assets() -> tuple[set[str], set[str]]:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    urls = set(re.findall(r'https?://[^\s<>")\]]+', text))
    assets = set(re.findall(r'(?:src|href)="([^":]+\.(?:svg|png|gif))"', text))
    assets |= set(re.findall(r"!\[[^\]]*\]\(([^):]+)\)", text))
    return urls, assets


def check_assets(assets: set[str]) -> None:
    for rel in sorted(assets):
        if (ROOT / rel).is_file():
            print(f"  ok   {rel}")
        else:
            failures.append(f"README references missing local file: {rel}")


def head(url: str) -> int:
    req = urllib.request.Request(url, headers=UA, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.status
    except urllib.error.HTTPError as exc:
        if exc.code == 405:  # HEAD not allowed; try GET
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                return resp.status
        return exc.code


def check_links(urls: set[str]) -> None:
    for url in sorted(urls):
        status = None
        for _ in range(2):  # one retry on transient failure
            try:
                status = head(url)
                break
            except (urllib.error.URLError, TimeoutError, OSError):
                continue
        if status is None:
            failures.append(f"unreachable: {url}")
        elif status < 400:
            print(f"  ok   {status} {url}")
        elif status in SOFT_STATUS:
            warnings.append(f"{status} {url}")
        else:
            failures.append(f"{status} {url}")


def main() -> int:
    print("svg assets:")
    check_svgs()
    urls, assets = readme_urls_and_assets()
    print("local assets referenced by README:")
    check_assets(assets)
    print("readme links:")
    check_links(urls)

    for w in warnings:
        print(f"  warn {w}")
    if failures:
        for f in failures:
            print(f"  FAIL {f}", file=sys.stderr)
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
