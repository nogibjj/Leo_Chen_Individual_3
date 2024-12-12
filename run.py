from app import create_app
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("WEBSITES_PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=os.getenv("FLASK_ENV") == "development")
