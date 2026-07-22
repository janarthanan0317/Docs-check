"""Minimal Flask application with a health-check endpoint."""

from flask import Flask


def create_app() -> Flask:
    """Create and configure the application instance."""
    app = Flask(__name__)

    @app.get("/health")
    def health() -> dict[str, str]:
        """Report that the service is running."""
        return {"status": "ok", "version": "v2"}

    return app


app = create_app()


if __name__ == "__main__":
    app.run()
