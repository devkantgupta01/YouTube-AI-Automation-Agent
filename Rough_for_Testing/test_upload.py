import os
from tools.upload_youtube import upload_video
from tools.generate_content import generate_video_content

#get video file
downloads_folder = "downloads"

video_file = None
script_file = None

for file in os.listdir(downloads_folder):
    if file.endswith(".mp4"):
        video_file = os.path.join(downloads_folder, file)
    elif file.endswith(".txt"):
        script_file = os.path.join(downloads_folder, file)

if not video_file or not script_file:
    print("Missing vidoe or script")
    exit()

#read script 
with open (script_file, "r", encoding="utf-8") as f:
    script = f.read()

#generate metadata
metadata = generate_video_content(script)

#upload video
video_url = upload_video(video_file, metadata)

print("\nUploaded Successfully!")
print("video URL:", video_url)