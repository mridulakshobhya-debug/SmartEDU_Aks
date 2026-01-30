#!/usr/bin/env python
import os
import sys
import logging

# Change to the project root directory
project_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(project_root)

# Add backend to path
sys.path.insert(0, os.path.join(project_root, 'backend'))

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Now import and run
try:
    from backend.app import create_app
    
    if __name__ == "__main__":
        logger.info("Creating Flask app...")
        app = create_app()
        logger.info("Flask app created successfully")
        logger.info("Starting server on http://127.0.0.1:5000")
        app.run(debug=False, host="0.0.0.0", port=5000, use_reloader=False, threaded=True)
except Exception as e:
    logger.error(f"Failed to start server: {e}", exc_info=True)
    sys.exit(1)
