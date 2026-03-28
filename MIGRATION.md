# CAClaw Migration Map

This file explains what belongs inside this repository and what should stay outside it.

## Keep inside CAClaw

These are good fits for the add-on:

- CA workflow skills and checklists
- CA task-routing prompts
- CA reference docs
- CA brand assets for this add-on
- CA MCP connection recipes
- CA integration contracts
- future secure connectors for GST, tax, audit, reporting, reconciliation, and compliance support

## Keep outside CAClaw

These do not need to live in the add-on repo:

- full-product OpenClaw branding changes
- global UI renames across the main OpenClaw product
- bundle-id and package-id changes in OpenClaw apps
- unrelated OpenClaw core logic

## Rework over time

Some docs in this repo started as migration material from the older CAClaw fork work.
They have been brought here because the ideas are still useful, but they should keep getting simpler and more practical over time.

## Simple rule

If the change makes OpenClaw more useful for Chartered Accountant workflows without turning this repo into a separate full product, it probably belongs here.
