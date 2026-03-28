import { definePluginEntry, type OpenClawPluginApi } from "./runtime-api.js";

export default definePluginEntry({
  id: "caclaw",
  name: "CAClaw",
  description: "Plugin-shipped Chartered Accountant workflow pack for OpenClaw.",
  register(_api: OpenClawPluginApi) {
    // CAClaw is intentionally skills-first.
    // Future CA MCP tools, prompts, and runtime services should land here
    // without requiring a deep OpenClaw product fork.
  },
});
