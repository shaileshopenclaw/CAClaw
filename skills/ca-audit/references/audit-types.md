# Audit Types Routing Guide

Use this guide to decide which audit branch should handle the request.

## Statutory audit

Choose this when the work refers to:

- Companies Act reporting
- Standards on Auditing
- CARO
- audit opinion drafting
- statutory audit planning, execution, or completion

Use: `ca-audit-statutory`

## Bank audit

Choose this when the work refers to:

- statutory branch audit (SBA)
- statutory central audit (SCA)
- bank advances audit
- NPA / IRACP norms
- provisioning review
- LFAR
- MOC
- treasury or investments audit for banks
- deposits and liabilities audit for banks
- RBI compliance

Use: `ca-audit-bank`

## Internal audit

Choose this when the work focuses on internal controls, process reviews, operational findings, or internal reporting.

## Tax audit

Choose this when the work is specifically tax-audit oriented and not a full statutory audit.

## Due diligence

Choose this for transaction review, buyer-side review, seller-side diligence, or special-purpose review work.

## Forensic or investigation work

Choose this when the work is about irregularities, fraud investigation, or evidence reconstruction.

## Rule of thumb

- If the user is asking for an opinion-linked audit workflow under Indian statutory-audit standards, route into `ca-audit-statutory`.
- If the user is asking for audit work specific to banks, RBI rules, LFAR, NPA, IRACP, SBA, or SCA, route into `ca-audit-bank`.
