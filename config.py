import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")

CREDENTIALS_FILE = "credentials/google_credentials.json"
TOKEN_FILE = "credentials/token.json"

SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/gmail.send"
]

DRIVE_ROOT_FOLDER_ID = "11q"