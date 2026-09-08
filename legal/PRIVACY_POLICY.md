# Privacy Policy — BlackMamba Template

Effective date: `[YYYY-MM-DD]`
Responsible party: `[LEGAL_OWNER_OR_ENTITY]`
Privacy contact: `[PRIVACY_CONTACT]`

This document is the reusable privacy baseline for BlackMamba projects. Each downstream project must replace placeholders and describe its real data flows before production use.

## 1. Data minimization

BlackMamba projects should collect and retain only the information reasonably necessary to provide the declared functionality, maintain security, diagnose failures, and satisfy applicable legal obligations.

If a feature can operate without identifying a person, identifying data should not be collected by default.

## 2. Possible categories of information

Depending on the project and deployment, processing may include:

- technical session identifiers;
- device, browser, operating-system, or application metadata;
- authentication and authorization metadata;
- security and abuse-prevention logs;
- telemetry expressly enabled by the operator;
- user-supplied configuration or content;
- transaction or billing records where commercially necessary.

A project-specific data inventory must state which of these categories are actually processed.

## 3. Purposes

Information may be processed to:

- provide requested functionality;
- authenticate and authorize access;
- maintain service integrity and security;
- detect abuse, fraud, or technical failures;
- improve reliability and performance;
- comply with applicable legal obligations.

Project-specific purposes must be documented before production deployment.

## 4. Sharing and processors

Personal data should not be sold as a default business practice. Transfers or disclosures to infrastructure providers, processors, or third parties must be documented in `THIRD_PARTY_NOTICES.md` or the applicable project-specific notice.

## 5. Retention

Retention must follow `DATA_RETENTION_POLICY.md`. Ephemeral data should remain ephemeral whenever persistent storage is unnecessary.

## 6. Security

Reasonable technical and organizational safeguards should be applied according to the sensitivity of the information and the risks of the deployment.

## 7. User rights and requests

Where Mexican data-protection law applies, the production notice and operating process must provide mechanisms for the rights and requests required by applicable law, including access, rectification, cancellation, and opposition where applicable.

## 8. Changes

Material changes to a production privacy notice should be versioned and communicated through an appropriate channel.

## 9. Template warning

This file is a framework, not a representation that every BlackMamba project processes the categories above. Final text must match the software's actual behavior and be reviewed for the applicable jurisdiction and business model.
