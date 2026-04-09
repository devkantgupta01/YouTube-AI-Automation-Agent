from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os
from config import CREDENTIALS_FILE, TOKEN_FILE, SCOPES

creds = None

# Load existing token if available
if os.path.exists(TOKEN_FILE):
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

# If no valid credentials, request login
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            CREDENTIALS_FILE, SCOPES
        )
        creds = flow.run_local_server(port=0)

    # Save token for future use
    with open(TOKEN_FILE, "w") as token:
        token.write(creds.to_json())

print("Authentication successful!")

# Test Drive API
drive_service = build("drive", "v3", credentials=creds)
results = drive_service.files().list(pageSize=1).execute()
print("Drive API working!")

# Test YouTube API
youtube_service = build("youtube", "v3", credentials=creds)
print("YouTube API working!")

# Test Gmail API
gmail_service = build("gmail", "v1", credentials=creds)
print("Gmail API working!")