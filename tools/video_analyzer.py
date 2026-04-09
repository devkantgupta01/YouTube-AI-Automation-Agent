from moviepy import VideoFileClip

def analyze_video(video_path):

    clip = VideoFileClip(video_path)
    duration = clip.duration #duration in second

    clip.close()

    if duration <= 60:
        video_type = "short"
    else:
        video_type = "long"

    return {
    "duration" : duration,
        "type" : video_type

    }
