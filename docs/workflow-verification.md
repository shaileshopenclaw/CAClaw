# CA Workflow Verification

Use this checklist to confirm that the CA workflow pack is present and usable.

## Verify the main skills exist

- `skills/ca-gst/SKILL.md`
- `skills/ca-tds/SKILL.md`
- `skills/ca-income-tax/SKILL.md`
- `skills/ca-audit/SKILL.md`
- `skills/ca-financial-reporting/SKILL.md`
- `skills/ca-roc-compliance/SKILL.md`
- `skills/ca-workbench/SKILL.md`

## Verify reusable content exists

Each domain should include:

- a reference file
- an asset such as a checklist or reusable working draft

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
