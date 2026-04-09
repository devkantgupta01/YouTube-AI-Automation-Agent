from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io
import os
from config import DRIVE_ROOT_FOLDER_ID
from config import SCOPES, TOKEN_FILE
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow


# def get_drive_service():
#     cred = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
#     return build("drive", "v3", credentials=cred)

def get_drive_service():
    creds = None

    # If token exists → load it
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    # If no valid creds → login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials/google_credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save new token
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    return build("drive", "v3", credentials=creds)

def get_subfolder_id(service, parent_id, folder_name):
    query = f"'{parent_id}' in parents and name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
    results = service.files().list(q=query, fields="files(id, name)").execute()
    folders = results.get("files", [])
    return folders[0]["id"] if folders else None


def get_video_and_script(service, input_folder_id):
    query = f"'{input_folder_id}' in parents and trashed=false"
    results = service.files().list(q=query, fields="files(id, name)").execute()
    files = results.get("files", [])

    video = None
    script = None

    for file in files:
        if file["name"].endswith(".mp4"):
            video = file
        elif file["name"].endswith(".txt"):
            script = file

    return video, script

def download_file(service, file_id, file_name, save_path="downloads"):
    os.makedirs(save_path, exist_ok=True)
    request = service.files().get_media(fileId=file_id)
    file_path = os.path.join(save_path, file_name)

    with io.FileIO(file_path, "wb") as fh:
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()

    return file_path


def move_file(service, file_id, new_parent_id):
    file = service.files().get(fileId=file_id, fields="parents").execute()
    previous_parents = ",".join(file.get("parents"))
    service.files().update(
        fileId=file_id,
        addParents=new_parent_id,
        removeParents=previous_parents
    ).execute()