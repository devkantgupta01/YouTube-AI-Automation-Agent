from tools.send_email import send_email

#dummy test data
video_url = "https://www.youtube.com/watch?v=DEVKANT01"

metadata = {
    "title" : "test video",
    "category": "technology",
    "tags": ["ai", "automation", "devgupta", "python"]
}

send_email(video_url, metadata)