# 🤖 YouTube AI Agent

An intelligent automation agent that automatically generates video metadata, analyzes video type, and uploads content to YouTube — all triggered from a Google Drive folder.

Built with Python, OpenAI API, and Google APIs.

---

## 🚀 What It Does

1. **Watches** a Google Drive `input/` folder for a video + script file
2. **Generates** YouTube title, description, and tags using GPT-4o
3. **Analyzes** the video to detect if it's a Short or a long-form video
4. **Uploads** the video to YouTube with the generated metadata
5. **Sends** an email notification with the YouTube link
6. **Moves** the processed files to a `used/` folder in Drive

---

## 🗂️ Project Structure

```
youtube-ai-agent/
│
├── assets/                    # Static assets
├── credentials/               # ⚠️ NOT included — add your own (see setup)
│   ├── google_credentials.json
│   └── token.json
│
├── tools/                     # Core modules
│   ├── drive_handler.py       # Google Drive operations
│   ├── generate_content.py    # GPT-4o metadata generation
│   ├── video_analyzer.py      # Short vs Long video detection
│   ├── upload_youtube.py      # YouTube Data API upload
│   └── send_email.py          # Email notification
│
├── Rough_for_Testing/         # Test scripts
│   ├── auth_test.py
│   ├── test_ai.py
│   ├── test_drive.py
│   ├── test_email.py
│   ├── test_upload.py
│   └── test_video.py
│
├── agent.py                   # Main entry point
├── config.py                  # Configuration variables
├── requirements.txt           # Python dependencies
└── .env                       # ⚠️ NOT included — add your own (see setup)
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/youtube-ai-agent.git
cd youtube-ai-agent
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here

EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password_here
EMAIL_RECEIVER=receiver_email@gmail.com

DRIVE_ROOT_FOLDER_ID=your_google_drive_folder_id_here
```

> **Note:** For Gmail, use an [App Password](https://support.google.com/accounts/answer/185833), not your regular password.

### 5. Set Up Google Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable the following APIs:
   - Google Drive API
   - YouTube Data API v3
   - Gmail API (optional)
4. Create **OAuth 2.0 credentials** and download the JSON file
5. Rename it to `google_credentials.json` and place it inside the `credentials/` folder
6. Run the agent once — it will open a browser window to authenticate and generate `token.json`

### 6. Set Up Google Drive Folder Structure

In your Google Drive, create a root folder with two subfolders:

```
📁 YourRootFolder/
├── 📁 input/      ← Drop your video + script here
└── 📁 used/       ← Agent moves processed files here
```

Copy the root folder ID from the Drive URL and paste it in `.env` as `DRIVE_ROOT_FOLDER_ID`.

---

## ▶️ Running the Agent

```bash
python agent.py
```

The agent will:
- Find the video and script from the `input/` folder
- Generate YouTube metadata using AI
- Upload the video
- Send an email notification
- Move files to `used/`

---

## 📦 Requirements

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Runtime |
| OpenAI API | Title, description, tags generation |
| Google Drive API | File management |
| YouTube Data API v3 | Video upload |
| Gmail / SMTP | Email notification |

Install all Python packages:

```bash
pip install -r requirements.txt
```

---

## 🔐 Security Notes

- **Never push** `credentials/`, `token.json`, or `.env` to GitHub
- Your `.gitignore` should include:

```
.env
credentials/
token.json
__pycache__/
downloads/
venv/
*.pyc
```

---

## 🛠️ Planned Features

- [ ] Thumbnail auto-generation using DALL·E 3
- [ ] Scheduler to run the agent automatically (APScheduler / cron)
- [ ] Support for multiple YouTube channels
- [ ] Web dashboard for monitoring uploads

---

## 🧑‍💻 Author

**Dev** — B.Tech CSE Student  
Built as a college project to explore LLM-based automation with real-world APIs.

Feel free to fork, star ⭐, and contribute!

---

## 📄 License

This project is licensed under the MIT License.
