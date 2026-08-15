#!/usr/bin/env python3
"""Validate the signed-snapshot structure without third-party dependencies."""

from __future__ import annotations

import base64
import hashlib
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / "registry-manifest.json"
SIGNATURE_PATH = ROOT / "registry-signature.json"


def registry_files() -> list[Path]:
    files = [ROOT / "index.json", ROOT / "security.json"]
    for directory in ("plugins", "icon-packs", "templates"):
        files.extend(
            path
            for path in (ROOT / directory).rglob("*")
            if path.is_file() and path.name not in {".gitkeep", ".DS_Store"}
        )
    files.extend(
        path
        for path in (ROOT / "certificates").glob("cert_*.*")
        if path.suffix in {".json", ".sig"}
    )
    return sorted(files, key=lambda path: path.relative_to(ROOT).as_posix())


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ValueError(f"{path.relative_to(ROOT)} is not valid UTF-8 JSON: {error}") from error


def validate_snapshot() -> list[str]:
    errors: list[str] = []
    manifest = load_json(MANIFEST_PATH)
    if not isinstance(manifest, dict):
        return ["registry-manifest.json must contain an object"]

    if manifest.get("schemaVersion") != 1:
        errors.append("registry-manifest.json schemaVersion must be 1")
    if not isinstance(manifest.get("sequence"), int) or manifest["sequence"] < 1:
        errors.append("registry-manifest.json sequence must be a positive integer")

    entries = manifest.get("files")
    if not isinstance(entries, list):
        return errors + ["registry-manifest.json files must be an array"]

    paths = [entry.get("path") for entry in entries if isinstance(entry, dict)]
    if len(paths) != len(entries) or any(not isinstance(path, str) for path in paths):
        return errors + ["every registry manifest entry must have a string path"]
    if paths != sorted(paths):
        errors.append("registry manifest entries must be sorted by path")
    if len(paths) != len(set(paths)):
        errors.append("registry manifest paths must be unique")

    expected = [path.relative_to(ROOT).as_posix() for path in registry_files()]
    missing = sorted(set(expected) - set(paths))
    unexpected = sorted(set(paths) - set(expected))
    if missing:
        errors.append(f"registry manifest is missing: {', '.join(missing)}")
    if unexpected:
        errors.append(f"registry manifest contains unexpected paths: {', '.join(unexpected)}")

    for entry in entries:
        if not isinstance(entry, dict) or not isinstance(entry.get("path"), str):
            continue
        relative = entry["path"]
        path = ROOT / relative
        if not path.is_file():
            continue
        content = path.read_bytes()
        actual_digest = hashlib.sha256(content).hexdigest()
        if entry.get("sha256") != actual_digest:
            errors.append(f"sha256 mismatch for {relative}")
        if entry.get("size") != len(content):
            errors.append(f"size mismatch for {relative}")

    return errors


def validate_signature_shape() -> list[str]:
    if not SIGNATURE_PATH.exists():
        print("Note: registry-signature.json is absent; the registry is not signed yet.")
        return []

    signature = load_json(SIGNATURE_PATH)
    if not isinstance(signature, dict):
        return ["registry-signature.json must contain an object"]

    errors: list[str] = []
    if signature.get("schemaVersion") != 1:
        errors.append("registry-signature.json schemaVersion must be 1")
    if signature.get("algorithm") != "ed25519":
        errors.append("registry-signature.json algorithm must be ed25519")
    key_id = signature.get("keyId")
    if not isinstance(key_id, str) or not (ROOT / "certificates" / f"{key_id}.json").is_file():
        errors.append("registry signature keyId must reference a published certificate")
    try:
        value = base64.b64decode(signature.get("value", ""), validate=True)
        if len(value) != 64:
            errors.append("registry signature value must decode to 64 bytes")
    except (TypeError, ValueError):
        errors.append("registry signature value must be valid base64")
    return errors


def main() -> int:
    errors: list[str] = []
    for path in sorted((ROOT / "schemas").glob("*.json")):
        try:
            load_json(path)
        except ValueError as error:
            errors.append(str(error))
    try:
        errors.extend(validate_snapshot())
        errors.extend(validate_signature_shape())
    except ValueError as error:
        errors.append(str(error))

    if errors:
        for error in errors:
            print(f"Error: {error}", file=sys.stderr)
        return 1

    print("Registry snapshot validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
