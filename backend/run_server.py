import os
import sys
import uvicorn
from pathlib import Path
from dotenv import load_dotenv

# Add app directory to path
sys.path.insert(0, str(Path(__file__).parent))

# Load environment variables from .env
load_dotenv(Path(__file__).parent / "app" / ".env")

if __name__ == "__main__":
    print("🚀 Starting DevMatch AI Backend Server...")
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )