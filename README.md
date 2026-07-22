# docs-test-app

A minimal Flask service that exposes `GET /health`.

## Run locally

```bash
python -m pip install -r requirements.txt
python app.py
```

The health endpoint returns `{"status": "ok", "version": "v2"}`.

`requirements.txt` and `sbom.json` are kept in sync; update both when changing a dependency.
