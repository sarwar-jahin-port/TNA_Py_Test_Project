# Agent Guidance

## GitHub Copilot Chat

Keep GitHub Copilot Chat available while disabling inline code suggestions. Configure this in VS Code User settings (JSON):

```json
{
  "github.copilot.enable": {
    "*": false
  }
}
```

Do not change application code or workspace behavior to control this preference. This disables automatic Copilot completions while leaving the Copilot Chat view available. Re-enable completions from the Copilot status-bar menu or the `GitHub Copilot: Enable Completions` command when needed.

## Project Basics

- Run the current smoke test with `python main.py`.
- There is no automated test suite or dependency manifest yet.
- Follow the project blueprint for the intended CLI behavior: [docs/E-Commerce CLI System (Version 1) - Comprehensive Team Blueprint & Execution Guide.md](docs/E-Commerce%20CLI%20System%20%28Version%201%29%20-%20Comprehensive%20Team%20Blueprint%20%26%20Execution%20Guide.md).