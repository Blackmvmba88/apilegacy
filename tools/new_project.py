#!/usr/bin/env python3
"""Generate a BlackMamba legal/security starter pack for a downstream project.

Usage:
    python3 tools/new_project.py project.json --out generated/my-project

No third-party Python dependencies are required.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SOURCE_FILES = {
    "LICENSE": ROOT / "LICENSE",
    "legal/API_TERMS.md": ROOT / "legal/API_TERMS.md",
    "legal/PRIVACY_POLICY.md": ROOT / "legal/PRIVACY_POLICY.md",
    "legal/ACCEPTABLE_USE_POLICY.md": ROOT / "legal/ACCEPTABLE_USE_POLICY.md",
    "legal/DATA_RETENTION_POLICY.md": ROOT / "legal/DATA_RETENTION_POLICY.md",
    "legal/THIRD_PARTY_NOTICES.md": ROOT / "legal/THIRD_PARTY_NOTICES.md",
    "security/SECURITY.md": ROOT / "security/SECURITY.md",
}

REQUIRED_TOP_LEVEL = {
    "project_name",
    "product_name",
    "repository_url",
    "brand_name",
    "legal_owner",
    "effective_date",
    "jurisdiction_primary",
    "license_mode",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def require_fields(config: dict) -> None:
    missing = sorted(k for k in REQUIRED_TOP_LEVEL if not config.get(k))
    if missing:
        raise SystemExit("Missing required fields: " + ", ".join(missing))

    unresolved = [
        k for k in ("legal_owner", "effective_date")
        if str(config.get(k, "")).strip().upper() in {"REPLACE_ME", "YYYY-MM-DD"}
    ]
    if unresolved:
        raise SystemExit(
            "Refusing to certify unresolved production fields: " + ", ".join(unresolved)
        )


def replacements(config: dict) -> dict[str, str]:
    privacy = config.get("privacy", {})
    security = config.get("security", {})
    return {
        "[LEGAL_OWNER]": str(config["legal_owner"]),
        "[LEGAL_OWNER_OR_ENTITY]": str(config["legal_owner"]),
        "[PRIVACY_CONTACT]": str(privacy.get("privacy_contact", "REPLACE_ME")),
        "[SECURITY_CONTACT]": str(security.get("security_contact", "REPLACE_ME")),
        "[YYYY-MM-DD]": str(config["effective_date"]),
        "BlackMamba Template": str(config["product_name"]),
    }


def render(text: str, mapping: dict[str, str]) -> str:
    for source, target in mapping.items():
        text = text.replace(source, target)
    return text


def build_manifest(config: dict, config_hash: str) -> dict:
    return {
        "schema": "blackmamba.legal-manifest/v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "project": {
            "name": config["project_name"],
            "product_name": config["product_name"],
            "repository": config["repository_url"],
            "effective_date": config["effective_date"],
        },
        "ownership": {
            "legal_owner": config["legal_owner"],
            "brand": config["brand_name"],
            "license": config["license_mode"],
        },
        "jurisdiction_primary": config["jurisdiction_primary"],
        "api": config.get("api", {}),
        "privacy": config.get("privacy", {}),
        "security": config.get("security", {}),
        "third_party": config.get("third_party", {}),
        "integrity": config.get("integrity", {}),
        "generation": {
            "source": "Blackmvmba88/apilegacy",
            "project_config_sha256": config_hash,
            "generator": "tools/new_project.py",
        },
        "certification": {
            "template_generated": True,
            "legal_counsel_reviewed": False,
            "production_approved": False,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate BlackMamba legal starter pack")
    parser.add_argument("config", type=Path, help="Path to project JSON configuration")
    parser.add_argument("--out", type=Path, required=True, help="Output directory")
    parser.add_argument(
        "--allow-placeholders",
        action="store_true",
        help="Allow REPLACE_ME/YYYY-MM-DD fields for draft generation only",
    )
    args = parser.parse_args()

    raw = args.config.read_bytes()
    config = json.loads(raw.decode("utf-8"))

    if args.allow_placeholders:
        missing = sorted(k for k in REQUIRED_TOP_LEVEL if not config.get(k))
        if missing:
            raise SystemExit("Missing required fields: " + ", ".join(missing))
    else:
        require_fields(config)

    mapping = replacements(config)
    args.out.mkdir(parents=True, exist_ok=True)

    generated_hashes: dict[str, str] = {}

    for relative, source in SOURCE_FILES.items():
        if not source.exists():
            raise SystemExit(f"Missing source template: {source}")

        destination = args.out / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        content = render(source.read_text(encoding="utf-8"), mapping)
        destination.write_text(content, encoding="utf-8")
        generated_hashes[relative] = sha256_bytes(content.encode("utf-8"))

    manifest = build_manifest(config, sha256_bytes(raw))
    manifest["generated_files_sha256"] = generated_hashes

    manifest_path = args.out / "LEGAL_MANIFEST.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(f"Generated BlackMamba legal pack: {args.out}")
    print(f"Manifest: {manifest_path}")


if __name__ == "__main__":
    main()
