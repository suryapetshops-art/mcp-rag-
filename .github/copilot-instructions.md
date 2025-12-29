# GitHub Copilot instructions for contributors

## Purpose ✅
Short, focused guidance for AI coding agents and contributors to be immediately productive in this repository.

## Big picture / architecture 🔧
- This is a minimal Streamlit app (single entrypoint: `app.py`) that demonstrates a RAG + MCP AI UI. There is no backend service or DB in this repository.
- UI and runtime live in `app.py`. External model/API calls are expected to be invoked from code added by contributors (no current LLM integration code exists).

## Quick start (what to run) ▶️
- Run locally: `streamlit run app.py`
- API key: set via environment variable `API_KEY` or enter it in the Streamlit sidebar (the app reads `os.getenv('API_KEY', '')` and stores it in `st.session_state['api_key']`).
- Note: `requirments.txt` currently contains the run command (`streamlit run app.py`) rather than a list of Python packages — treat it as a typo; if you add packages, create/update `requirements.txt` (correct spelling) and list package names.

## Key files to inspect 📁
- `app.py` — UI logic, page config, API-key handling, and the input field where user questions are collected.
- `services/llm.py` — **new**: minimal LLM client interface for provider integration (replace the stub `generate` method with your provider call).
- `README.md` — includes run and secret handling instructions.
- `requirements.txt` — lists runtime deps (added by contributors); note the old `requirments.txt` file contains a run command and is a typo.
- `requirments.txt` — informal run helper; does not list packages.

## Project-specific patterns & examples 💡
- API key handling (exact and discoverable):

```python
env_api_key = os.getenv("API_KEY", "")
if "api_key" not in st.session_state:
    st.session_state["api_key"] = env_api_key

sidebar_key = st.sidebar.text_input("API Key", value=st.session_state.get("api_key", ""), type="password")
```

- UI changes should be implemented directly in `app.py` or by adding small modules and importing them from `app.py`.
- Avoid printing secret values to the UI or logs — the code intentionally prints only presence/absence of the key.

## Integration points / external dependencies 🔗
- External LLM or retrieval services are not present; when adding them, follow these local rules:
  - Add code in a new module (e.g., `llm.py` or `services/`) and import into `app.py`.
  - Update `requirements.txt` (correctly spelled) with any new packages and document run/config steps in `README.md`.
  - Use environment variables for secrets (do not hard-code keys in source files).

## Secret handling & CI example 🔒
- Keep secrets out of the repo. If you accidentally commit a secret, **rotate it immediately** and remove it from history (see commands below).

- Local development options (examples):
  - Temporary (single command): `API_KEY="YOUR_API_KEY" streamlit run app.py`
  - Export for a session: `export API_KEY="YOUR_API_KEY"` then `streamlit run app.py`
  - Use a local `.env` file and a library like `python-dotenv` (ensure `.env` is in `.gitignore`). A provided `.env.example` shows the required variables.

- GitHub Actions example (use repo secret `API_KEY`):

```yaml
jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install
        run: pip install -r requirements.txt
      - name: Run Streamlit app (example)
        env:
          API_KEY: ${{ secrets.API_KEY }}
        run: streamlit run app.py
```

- Purging secrets from git history (high level):
  - If secret is only in uncommitted files: remove it and add to `.gitignore`.
  - If secret is committed and pushed: rotate the key immediately, then use tools like `git filter-repo` or `bfg` to purge it from history and force-push the cleaned repo. Coordinate with collaborators when rewriting history.

## Tests, CI, and linting ⚠️
- There are currently no tests, CI configuration, or linting tools in the repo. If you add tests, prefer `pytest` and place tests in a top-level `tests/` folder.

## PR checklist for small changes ✅
- Run `streamlit run app.py` and manually validate the new/changed UI behavior.
- If you add dependencies: update `requirements.txt` (fix the filename typo if needed) and `README.md` with install/run instructions.
- Keep secrets out of source (use env vars); do not echo full API keys in logs or UI.
- Keep changes small and focused — this is a tiny, single-file demo app.

## Interaction style for AI agents 🧭
- Propose specific, minimal code diffs and tests where applicable.
- Include exact file/line examples (e.g., show the small function or code snippet to add to `app.py`).
- When adding a new dependency, include the exact pip package and version to add to `requirements.txt`.

---

If anything here is unclear or you want more detail (e.g., suggested file layout for LLM integration, a sample `requirements.txt`, or a starter `services/llm.py`), tell me which area to expand and I will update this file.