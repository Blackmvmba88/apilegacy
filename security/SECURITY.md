# Security Policy — BlackMamba Template

Security contact: `[SECURITY_CONTACT]`

## Supported versions

Only versions explicitly marked as supported in release documentation are expected to receive security fixes.

## Reporting a vulnerability

A useful report should include:

- affected project and version;
- reproduction steps;
- expected behavior;
- observed behavior;
- security impact;
- logs or proof of concept where safe.

Do not include real credentials, secrets, or unnecessary personal data in reports.

## Baseline controls

Projects should implement, as applicable:

- secrets outside source control;
- least-privilege credentials;
- authenticated and expiring sessions;
- encrypted network transport;
- input validation;
- rate limiting and abuse controls;
- dependency and license review;
- structured security logging;
- credential revocation;
- reproducible release identifiers;
- cryptographic hashes for release artifacts;
- documented third-party trust boundaries.

## Secret handling

API keys, tokens, passwords, private keys, signing secrets, and production credentials must never be committed intentionally to public repositories.

Use environment variables, operating-system keychains, secret managers, or deployment-specific secure storage.

## Coordinated disclosure

Reporters should allow a reasonable opportunity to validate and remediate vulnerabilities before public disclosure, except where immediate disclosure is required by law or necessary to address imminent harm.

## Release rule

A release should not be labeled production-ready until its security checklist and legal manifest are complete for the intended deployment.
