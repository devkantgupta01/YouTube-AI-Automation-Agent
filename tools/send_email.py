from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from email.mime.text import MIMEText
import base64

from config import TOKEN_FILE, SCOPES, EMAIL_ADDRESS


def get_gmail_service():
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    return build("gmail", "v1", credentials=creds)


def send_email(video_url, metadata):

    service = get_gmail_service()

    subject = "🎬 Your YouTube Video Has Been Uploaded!"

    body = f"""
Your video has Benn SUccessfully uploaded...

Title : {metadata["title"]}
URL : {video_url}
Category: {metadata["category"]}
Tags: {", ".join(metadata["tags"])}

By :-
YouTube AI Agent devloped by devkantgupta01 (DE✌️)
"""

    message = MIMEText(body)
    message["to"] = EMAIL_ADDRESS
    message["from"] = EMAIL_ADDRESS
    message["subject"] = subject

    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    service.users().messages().send(
        userId="me",
        body={"raw": raw_message}
    ).execute()

    print("Email sent successfully!")