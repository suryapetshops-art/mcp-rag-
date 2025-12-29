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
