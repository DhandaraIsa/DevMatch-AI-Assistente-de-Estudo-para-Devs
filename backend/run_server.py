import os
import uvicorn

# Set environment variable
os.environ['GEMINI_API_KEY'] = 'AIzaSyCaCzdKalFdMOyokn-Sg8B7R1iC_Hsws-U'

if __name__ == "__main__":
    print("🚀 Starting DevMatch AI Backend Server...")
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8003,
        reload=False,
        log_level="info"
    )