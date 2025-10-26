# 🎬 PyMultiDL — Smart Multi-Threaded YouTube & File Downloader
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made with Love](https://img.shields.io/badge/made%20with-%E2%9D%A4-red.svg)](https://github.com/mscoder-py/pytray-reminder)

> ⚡ A fast, colorful, and intelligent downloader that supports **YouTube videos/playlists** and **web file URLs** using Python.  
> Built with ❤️ using `yt-dlp`, `colorama`, and `requests`.

---

## 🌟 Features
✅ Download YouTube videos or playlists (auto-merged in 720p)  
✅ Download direct files (images, documents, etc.) via URL  
✅ Real-time **progress bars** per download  
✅ Beautiful **colored CLI interface**  
✅ Automatic folder organization:
   - 📂 `/yt_videos` — YouTube downloads  
   - 📂 `/file` — Web files  
✅ Supports short YouTube links (`youtu.be/...`)  
✅ Auto-detects `ffmpeg` if installed  
✅ Multithreading for faster, smoother downloading  

---

## ⚠️ Usage Warning
- #### This tool is for educational and personal offline use only.
- #### Do NOT use it to download copyrighted or restricted material.
- #### Always respect YouTube and website terms of service.


---

## 🧠 Requirements
- 🐍 Python 3.8+
- 📦 Libraries: `yt-dlp`, `colorama`, `requests`
- 🎞️ Optional: `ffmpeg` (for video merging)

---

## ⚙️ Installation

```bash
# 1️⃣ Clone the repository
git clone https://github.com/yourusername/PyMultiDL.git
cd PyMultiDL

# 2️⃣ Install dependencies
pip install yt-dlp colorama requests

# 3️⃣ (Optional) Install ffmpeg
# Windows:
#   Download from https://ffmpeg.org and place in C:\ffmpeg\bin\ffmpeg.exe
# Linux/Mac:
sudo apt install ffmpeg
```
## ▶️ Usage Guide

- Run the program in your terminal:
```bash
python pymultidl.py
```
- Choose from the colorful menu:
```markdown
 1. YouTube Videos
 2. Web Files
Enter your choice:
```
### 🎥 Example 1: Download YouTube Videos
```markdown
Enter your choice: 1
How many YouTube URLs: 2
Enter URL 1: https://youtu.be/abc123
Enter URL 2: https://www.youtube.com/watch?v=xyz456


✅ The videos will be downloaded in the /yt_videos folder
with live progress bars like this:

🎬 Video 1:
████████████████████████████████████████ 100.0%
✅ Video 1 downloaded successfully.
```
## 🌐 Example 2: Download Web Files
```markdown
Enter your choice: 2
How many images to download: 2
Enter image URL 1: https://example.com/image1.jpg
Enter image URL 2: https://example.com/image2.png


📁 Saved automatically in the /file folder.

🧾 Example Output
🎬 Video 1:
████████████████████████████████████████ 100.0%
✅ Download Complete!

🎬 Video 2:
███████████████████..................... 72.4%
✅ Download Complete!

⚡ Total time: 43.2 sec
```
## 🧩 Tech Stack
### Component	Purpose
- 🐍 Python	Core Language
- 🎞️ yt-dlp	YouTube downloader engine
- 🌈 colorama	Colored terminal interface
- ⚡ concurrent.futures	Multithreading
- 🌐 requests	File downloads
### 📁 Folder Structure
```struture
PyMultiDL/
├── pymultidl.py
├── yt_videos/
│   ├── video1.mp4
│   └── video2.mp4
├── file/
│   ├── file1.jpg
│   └── file2.png
└── README.md
```
## 📊 Example CSV Output (if extended logging is enabled)
| File Name  | URL                                                              | Status      | Time |
| ---------- | ---------------------------------------------------------------- | ----------- | ---- |
| video1.mp4 | [https://youtu.be/abc123](https://youtu.be/abc123)               | ✅ Completed | 25s  |
| file1.jpg  | [https://example.com/image1.jpg](https://example.com/image1.jpg) | ✅ Completed | 3s   |

### 🎬 PyMultiDL — Multi-threaded Downloader
```cli
⚠️ WARNING: Educational use only.
✅ Ready to download videos and files!

🎥 Video 1:
████████████████████████████████████████ 100%
✅ Video 1 downloaded successfully!
```
## 🧩 Future Ideas

 - GUI version using PyQt / Tkinter

 - Download resuming

 - Detailed logging system

 ## 👨‍💻 Author

- ### Made with ❤️ by MS Coder
- #### Version: v1.0
## 💬 Feedback

- Found a bug or want to contribute?
- 💡 Open an issue or submit a pull request here:
- 👉 GitHub Issues

### Python License: MIT — Made with ❤️ by MS Coder


