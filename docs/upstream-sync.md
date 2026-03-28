# Updating CAClaw When OpenClaw Changes

This page explains a simple way to keep CAClaw aligned with OpenClaw.

## Goal

Keep CAClaw compatible with OpenClaw without turning CAClaw into a deep fork.

## Simple update workflow

1. check what changed in OpenClaw
2. identify whether those changes affect plugin install, runtime behavior, skills, or docs
3. update CAClaw only where needed
4. verify the install flow again
5. verify the main CA skills still make sense

## Areas to watch carefully

Pay extra attention if OpenClaw changes:

- plugin installation behavior
- plugin metadata requirements
- runtime plugin registration behavior
- skill-loading behavior
- plugin security or sandbox expectations

## Minimum re-check after an OpenClaw update

```bash
openclaw plugins install .
openclaw plugins enable caclaw
openclaw plugins inspect caclaw
```

If those still work, the add-on relationship is usually in a healthy place.
