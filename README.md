# mcp-rag-

Minimal Streamlit demo for RAG + MCP AI.

## Running locally

Set your API key as an environment variable (do not commit it):

- Temporary (single command):
  `API_KEY="YOUR_API_KEY" streamlit run app.py`

- Export for the session:
  `export API_KEY="YOUR_API_KEY"`
  `streamlit run app.py`

Alternatively create a `.env` file with `API_KEY=...` and ensure `.env` is listed in `.gitignore`.

## Install dependencies

If you want to run the app in a virtual environment or add integrations, install the project's dependencies:

- `pip install -r requirements.txt`

(If you're upgrading or adding packages, update `requirements.txt` and mention the change in your PR.)

## Security note

Do not commit secrets to the repository. If a secret is accidentally committed, rotate it immediately and remove it from history (see below or consult your provider's docs).

### Adding the repository secret (recommended) 🔒

- **GitHub UI**:
  1. Go to your repo → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**.
  2. Name: `API_KEY`, Value: your API key, then **Add secret**.

- **gh CLI**:
  - Safer (avoids shell history):
    `echo -n "YOUR_API_KEY" | gh secret set API_KEY --repo suryapetshops-art/mcp-rag-`
  - Or non-interactive:
    `gh secret set API_KEY -b"YOUR_API_KEY" --repo suryapetshops-art/mcp-rag-`

> **Security note:** If you pasted a key in chat or elsewhere, rotate it immediately and replace it with a new key.
