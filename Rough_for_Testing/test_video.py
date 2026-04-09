import os
from tools.video_analyzer import analyze_video

download_folder = "downloads"

video_file = None

#find mp4 automatically
for file in os.listdir(download_folder):
    if file.endswith(".mp4"):
        video_file = os.path.join(download_folder, file)
        break

if not video_file:
    print("no video found. ")
    exit()

result = analyze_video(video_file)

print("\nVideo Analysis:\n")

print("Duration: ", round(result["duration"], 2), "seconds")
print("video Type:", result["type"])

