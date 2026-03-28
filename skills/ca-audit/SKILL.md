---
name: ca-audit
description: Audit main branch for CAClaw. Use when the user needs audit help and you first need to identify the audit type before routing into the right audit workflow.
---

# CA Audit Main Branch

Use this skill as the **main audit branch**.

## What to do

1. First identify the audit type.
2. Common audit branches include:
   - statutory audit
   - bank audit
   - internal audit
   - tax audit
   - due diligence review
   - forensic or investigation work
   - limited review or certification support
3. If the work is **statutory audit**, use the dedicated `ca-audit-statutory` branch.
4. If the work is **bank audit**, use the dedicated `ca-audit-bank` branch.
5. If the work is another audit type, keep the guidance general for now and clarify the exact audit objective before proceeding.
6. Use `references/audit-types.md` to structure the branching decision.
7. Use `assets/audit-checklist.md` when the user needs a simple audit prep checklist.

## Boundaries

- Do not assume every audit request is statutory audit.
- Do not assume every audit request is bank audit.
- Do not imply final assurance conclusions are produced automatically.
- Keep outputs review-oriented and human-supervised.
