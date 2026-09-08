# Data Retention Policy — BlackMamba Template

## Principle

Retain information only for as long as reasonably necessary for the documented purpose, security requirement, contractual obligation, or applicable legal obligation.

## Default classes

| Data class | Example | Baseline posture |
|---|---|---|
| Ephemeral input | motion/gamepad packets | memory/session only |
| Session metadata | temporary session identifier | session + short operational grace period |
| Security logs | auth failures, abuse events | project-defined, minimized |
| Telemetry | performance/error events | opt-in or documented operational need |
| User content | configuration/files | until deletion or defined lifecycle |
| Commercial records | invoices/payment evidence | applicable accounting/legal period |

## Requirements

Each production project must document:

1. the exact fields retained;
2. the purpose of retention;
3. the retention duration or deletion trigger;
4. where the information is stored;
5. who or what can access it;
6. whether a third party processes or stores it;
7. how deletion or anonymization is performed.

## Ephemeral-first rule

If a function can be implemented without persistence, persistence should not be introduced merely for convenience.

## Backups

Backup retention must be documented separately when deletion from primary storage does not immediately remove all backup copies.

## Exceptions

A project may retain information longer when reasonably necessary for fraud prevention, security investigation, dispute handling, accounting, or applicable legal obligations, provided the exception is documented and access remains appropriately restricted.
