# CA Workflow Verification

Use this checklist to confirm that the CA workflow pack is present and usable.

## Verify the main skills exist

- `skills/ca-gst/SKILL.md`
- `skills/ca-tds/SKILL.md`
- `skills/ca-income-tax/SKILL.md`
- `skills/ca-audit/SKILL.md`
- `skills/ca-audit-statutory/SKILL.md`
- `skills/ca-audit-bank/SKILL.md`
- `skills/ca-financial-reporting/SKILL.md`
- `skills/ca-roc-compliance/SKILL.md`
- `skills/ca-workbench/SKILL.md`

## Verify reusable content exists

Each domain should include:

- a reference file
- an asset such as a checklist or reusable working draft

For statutory audit specifically, verify that:

- `skills/ca-audit-statutory/references/commands/` exists
- `skills/ca-audit-statutory/references/guides/` exists
- `skills/ca-audit-statutory/references/knowledge/` exists
- `skills/ca-audit-statutory/assets/statutory-audit-start-checklist.md` exists

For bank audit specifically, verify that:

- `skills/ca-audit-bank/references/` exists
- `skills/ca-audit-bank/checklists/` exists
- `skills/ca-audit-bank/assets/` exists
- `skills/ca-audit-bank/scripts/` exists

## Suggested checks

```bash
find skills/ca-* -maxdepth 2 -type f | sort
openclaw plugins inspect caclaw
```

## Completion standard

CAClaw is in good shape when:

- all main skills exist
- references and assets exist
- the plugin installs correctly into OpenClaw
- the workflow pack is easy to understand and use
