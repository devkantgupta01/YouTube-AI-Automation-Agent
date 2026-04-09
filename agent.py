# import os
# from tools import generate_content;
# from tools import generate_thumbnail;
# from tools.video_analyzer import analyze_video;

# video_info = analyze_video(video_path)

# if video_info["type"] == "short":
#     print("Short video detected - skipping thumbnail")

# else:
#     print("Long video - generating thumbnail")
#     thumbnail_path = generate_thumbnail(metadata)

import os
from tools.drive_handler import(
    get_drive_service,
    get_subfolder_id,
    get_video_and_script,
    download_file,
    move_file
)

from tools.generate_content import generate_video_content
from tools.video_analyzer import analyze_video
# from tools.generate_thumbnail import generate_thumnail
from tools.upload_youtube import upload_video
from tools.send_email import send_email

from config import DRIVE_ROOT_FOLDER_ID

def run_agent():
# -------------------------------------------------------------------------------
    print("\n Agent started....\n")

    service = get_drive_service()

    # get folders
    input_folder_id = get_subfolder_id(service, DRIVE_ROOT_FOLDER_ID, "input")
    used_folder_id = get_subfolder_id(service, DRIVE_ROOT_FOLDER_ID, "used")

    if not input_folder_id or not used_folder_id:
        print("Folder structure not found...|||")
        return
    
    # find files
    video, script = get_video_and_script(service, input_folder_id)

    if not video or not script:
        print("No Valid video & script folund...|||")
        return
    
# ------------------------------------------------------------------------------
    print("Dounloading files....>>>")
   
    video_path = download_file(service, video["id"], video["name"])
    script_path = download_file(service, script["id"], script["name"])

    # read script
    with open(script_path, "r", encoding="utf-8") as f:
        script_text = f.read()

    
# ------------------------------------------------------------------------------
    print("Generating Content~~~~")
    metadata = generate_video_content(script_text)
   
# -------------------------------------------------------------------------------
    print("Analyzing video....")
    video_info = analyze_video(video_path)

      # shorts logic
    if video_info["type"] == "short":
        print("Short video detected → skipping thumbnail")
    else:
        print("Long video → thumbnail generation (skip for now)")
# --------------------------------------------------------------------------------
    print("Uploading to YouTube...")

    video_url = upload_video(video_path, metadata)
# ---------------------------------------------------------------------------------
    print("Sending email....@")

    send_email(video_url, metadata)
# ---------------------------------------------------------------------------------
    print("Moving files to 'used' folder" )
    move_file(service, video["id"], used_folder_id)
    move_file(service, script["id"], used_folder_id)

# ----------------------------------------------------------------------------------------

    print("\n workflow complete successully. \n")

if __name__ == "__main__":
    run_agent()


