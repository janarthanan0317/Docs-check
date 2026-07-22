@app.route("/health")
def health():
    return {"status": "ok", "version": "v2"}