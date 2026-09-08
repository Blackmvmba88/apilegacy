# Mexico Legal Baseline — API Legacy

> Working baseline for engineering and documentation. This is not a substitute for legal advice tailored to a specific product, company structure, contract, or processing activity.

## 1. Personal data

The primary federal baseline for private-sector personal-data processing in Mexico is the **Ley Federal de Protección de Datos Personales en Posesión de los Particulares** issued by decree published in the Diario Oficial de la Federación on **20 March 2025**.

Engineering consequence: a production project that processes personal data must not ship with a generic privacy file that contradicts its actual behavior. The project must inventory what it collects, why, where it is stored, who receives it, and how long it is retained.

BlackMamba default: **data minimization and ephemeral-first processing**.

Official source:
- Diario Oficial de la Federación — decree of 20 March 2025: https://www.dof.gob.mx/nota_detalle.php?codigo=5752569&fecha=20/03/2025

## 2. Trademarks and brand

Distinctive signs used commercially in Mexico can be protected through the **Instituto Mexicano de la Propiedad Industrial (IMPI)**. Trademark registrations are generally granted for ten-year periods and may be renewed subject to the applicable requirements.

Engineering/business consequence: repository names, package names, domains, visual identity, and product names should be checked before assuming that a brand name is legally available for commercial use.

Official sources:
- IMPI trademark information: https://www.gob.mx/impi/documentos/registro-de-marcas
- IMPI trademark FAQ: https://www.gob.mx/impi/acciones-y-programas/temas-de-interes-preguntas-frecuentes-marcas

## 3. Copyright and software

Software source code and related authorship records should be managed as intellectual-property assets. For projects selected for formal registration, the working process should preserve a reproducible source package, version, commit, date, authorship/titular information, and cryptographic hash.

INDAUTOR provides registration procedures and forms for copyright works and related acts.

Official source:
- INDAUTOR registration guides: https://www.indautor.gob.mx/servicios/guias_registro.php

## 4. Third-party software and services

Public availability does not equal unrestricted commercial permission. Every production project should maintain an inventory of libraries, APIs, services, assets, and trademarks it uses and record the applicable license or terms.

## 5. Evidence chain for important releases

For a release selected as an important legal/IP checkpoint, preserve at minimum:

1. product and repository name;
2. semantic version or release identifier;
3. Git commit SHA;
4. release date;
5. source package hash (SHA-256);
6. artifact hash where applicable;
7. declared owner/titular;
8. applicable license;
9. third-party inventory;
10. privacy/data inventory;
11. security review status;
12. copy of the legal manifest.

## 6. What this repository does not do

API Legacy does not itself:

- register a trademark;
- register software with INDAUTOR;
- create a corporation;
- obtain regulatory approval;
- guarantee compliance with third-party platform terms;
- replace counsel for commercial contracts, employment/IP assignments, investment, consumer law, tax, or international expansion.

Its purpose is to ensure BlackMamba software is born with the documentation and technical evidence needed to make those formal processes much cleaner.
