#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DENIED_SUFFIXES = {
    ".cpp", ".c", ".cc", ".cxx", ".h", ".hpp", ".inl",
    ".uasset", ".umap", ".uproject", ".uplugin",
    ".dll", ".exe", ".pdb", ".lib", ".obj",
    ".pak", ".ucas", ".utoc",
    ".zip", ".rar", ".7z",
    ".pem", ".pfx", ".p12", ".key",
}

DENIED_NAMES = {".env", "credentials.json", "client_secret.json"}

ALLOW_PATHS = {Path("scripts/public_safety.py")}

TEXT_SUFFIXES = {
    ".md", ".txt", ".yml", ".yaml", ".json", ".toml",
    ".ini", ".cfg", ".css", ".js", ".html", ".xml", ".py",
}

SUSPICIOUS_PATTERNS = [
    re.compile(r"VerseAtile_Frameworks[/\\\\]Development[/\\\\]RiZRoC", re.I),
    re.compile(r"Plugins[/\\\\]RiZRoC[/\\\\]Source", re.I),
    re.compile(r"BEGIN (RSA|EC|OPENSSH|PRIVATE) PRIVATE KEY", re.I),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"(?i)\b(client_secret|api[_-]?key|access[_-]?token|refresh[_-]?token|password)\b\s*[:=]\s*[\"'][^\"']{8,}[\"']"),
]

errors: list[str] = []

for path in ROOT.rglob("*"):
    if not path.is_file():
        continue

    rel = path.relative_to(ROOT)
    if rel.parts and rel.parts[0] in {".git", "site", "__pycache__"}:
        continue

    rel_norm = Path(*rel.parts)

    if rel_norm not in ALLOW_PATHS:
        if path.name.lower() in DENIED_NAMES:
            errors.append(f"DENIED file name: {rel}")
        if path.suffix.lower() in DENIED_SUFFIXES:
            errors.append(f"DENIED private/source/binary file type: {rel}")

    if path.suffix.lower() in TEXT_SUFFIXES or path.name in {"NOTICE.md", "PUBLIC_CONTENT_POLICY.md"}:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in SUSPICIOUS_PATTERNS:
            if pattern.search(text):
                if rel_norm == Path("PUBLIC_CONTENT_POLICY.md") and "VerseAtile_Frameworks" in pattern.pattern:
                    continue
                errors.append(f"Suspicious private path/secret pattern in: {rel}")
                break

if errors:
    print("PUBLIC SAFETY GATE: FAIL", file=sys.stderr)
    for error in errors:
        print(f" - {error}", file=sys.stderr)
    sys.exit(1)

print("PUBLIC SAFETY GATE: PASS")
