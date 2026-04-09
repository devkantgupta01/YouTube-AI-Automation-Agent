from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
from config import TOKEN_FILE, SCOPES

#map catogery names into youtube category ids
CATEGORY_MAP = {
    "Education": 27,
    "Entertainment": 24,
    "Technology": 28,
    "Howto & Style": 26,
    "Science & Technology": 28
}

def get_youtube_service():
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    return build("youtube", "v3", credentials=creds)

def upload_video(video_path, metadata):
    
    youtube = get_youtube_service()

    category_id = CATEGORY_MAP.get(metadata["category"],28)
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": metadata["title"],
                "description": "\n".join(metadata["hashtags"]),
                "tags": metadata["tags"],
                "categoryId": str(category_id)
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=MediaFileUpload(video_path)
    )

    response = request.execute()

    video_id = response["id"]

    video_url = f"https://www.youtube.com/watch?v={video_id}"

    return video_url