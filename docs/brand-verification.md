# CAClaw Brand Verification

Use this checklist when you want to confirm that the CAClaw brand is presented clearly and consistently.

## Check these files

- `README.md`
- `package.json`
- `openclaw.plugin.json`
- `index.ts`
- `assets/caclaw-logo-text.svg`
- `assets/caclaw-logo-text-dark.svg`

## What should be true

- the repo presents itself as **CAClaw**
- the repo also clearly says it is **for OpenClaw**
- the assets visibly show the CAClaw name
- installation still points to the standard OpenClaw plugin flow

## Quick verification commands

```bash
grep -n 'CAClaw\|OpenClaw' README.md package.json openclaw.plugin.json index.ts
grep -n 'CAClaw' assets/caclaw-logo-text.svg assets/caclaw-logo-text-dark.svg
```
