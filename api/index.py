import os
import sys
from pathlib import Path

# Ensure project root is importable
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.app import create_app  # noqa: E402


def _default_env() -> str:
    if os.getenv("FLASK_ENV"):
        return os.getenv("FLASK_ENV", "production")
    return "production" if os.getenv("VERCEL") else "development"


# Vercel expects a WSGI callable named `app`
app = create_app(_default_env())

