import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.app import create_app  # noqa: E402

def _default_env():
    return "production" if os.getenv("VERCEL") else "development"

app = create_app(_default_env())
