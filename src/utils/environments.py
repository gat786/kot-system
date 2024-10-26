from dotenv import load_dotenv
import os

load_dotenv()

DEV_ENVIRONMENT = "development"
SERVER_HOST   = os.getenv("SERVER_HOST", "0.0.0.0")
SERVER_PORT   = os.getenv("SERVER_PORT", "8000")
ENVIRONMENT   = os.getenv("ENVIRONMENT", DEV_ENVIRONMENT)
