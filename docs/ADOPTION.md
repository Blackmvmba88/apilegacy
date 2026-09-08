# Adopting API Legacy in a BlackMamba Project

## Goal

Every new BlackMamba program should receive the same minimum legal/security skeleton without rewriting it manually.

## Recommended flow

1. Clone or reference `Blackmvmba88/apilegacy`.
2. Copy `templates/project.template.json` to a project-specific config file.
3. Replace all required placeholders.
4. Run the generator:

```bash
python3 tools/new_project.py path/to/project.json --out path/to/project
```

5. Review the generated files against the actual behavior of the target program.
6. Complete the third-party inventory.
7. Complete the data inventory and retention decisions.
8. Add release identifiers and hashes.
9. Obtain legal review when the project is commercial, high-risk, handles meaningful personal data, or enters contracts with customers/partners.

## Draft mode

For prototyping only, unresolved placeholders can be allowed:

```bash
python3 tools/new_project.py path/to/project.json --out path/to/project --allow-placeholders
```

Draft mode must not be treated as production certification.

## Minimum generated pack

A downstream project should receive:

```text
LICENSE
LEGAL_MANIFEST.json
legal/
  API_TERMS.md
  PRIVACY_POLICY.md
  ACCEPTABLE_USE_POLICY.md
  DATA_RETENTION_POLICY.md
  THIRD_PARTY_NOTICES.md
security/
  SECURITY.md
```

## Project truth wins

Generated text is a starting point. If the software collects data, exposes capabilities, stores logs, performs automation, or integrates with third parties differently from what the template says, the documents must be changed to match reality.

## Release gate

Before labeling a downstream project production-ready, verify:

- no unresolved `REPLACE_ME` fields;
- owner/titular is correct;
- privacy contact and security contact are valid;
- actual data collection is documented;
- retention is documented;
- third-party licenses and terms were reviewed;
- credentials are not committed;
- release commit and hashes are recorded;
- legal review status is explicit rather than implied.
