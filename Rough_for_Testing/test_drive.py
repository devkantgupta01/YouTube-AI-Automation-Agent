from tools.drive_handler import (
    get_drive_service,
    get_subfolder_id,
    get_video_and_script,
    download_file
)

from config import DRIVE_ROOT_FOLDER_ID


def main():
    service = get_drive_service()

    # find input folder
    input_folder_id = get_subfolder_id(
        service,
        DRIVE_ROOT_FOLDER_ID,
        "input"
    )

    if not input_folder_id:
        print("Input folder not found.")
        return

    print("Input folder ID:", input_folder_id)

    # detect video and script
    video, script = get_video_and_script(service, input_folder_id)

    if not video or not script:
        print("Video or script not found.")
        return

    print("Video found:", video["name"])
    print("Script found:", script["name"])

    # download files
    video_path = download_file(service, video["id"], video["name"])
    script_path = download_file(service, script["id"], script["name"])

    print("Downloaded video:", video_path)
    print("Downloaded script:", script_path)


if __name__ == "__main__":
    main()