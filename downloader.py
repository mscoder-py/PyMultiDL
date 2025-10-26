__version__ = "1.0"

import os
import sys
import threading
import requests
import concurrent.futures
import yt_dlp
import colorama
import time
from urllib.parse import urlparse, parse_qs

# Initialize colorama
colorama.init()
print_lock = threading.Lock()

# ────────────────────────────────
# 🎨 COLOR UTILITY
# ────────────────────────────────
def colorize(text, color):
    colors = {
        "GREEN": "\033[32m",
        "GREEN_BOLD": "\033[1;32m",
        "RED_BOLD": "\033[1;31m",
        "CYAN_BOLD": "\033[1;36m",
        "YELLOW_BOLD": "\033[1;33m",
        "MAGENTA_BOLD": "\033[1;35m",
        "RESET": "\033[0m",
    }
    return f"{colors.get(color, '')}{text}{colors['RESET']}"

# ────────────────────────────────
# ⚠️ WARNING BOX
# ────────────────────────────────
def show_warning_box():
    print(colorize("Code_By :", "GREEN_BOLD") + colorize(" MS Coder", "YELLOW_BOLD"))
    print(colorize("Version :", "GREEN_BOLD") + colorize(" v1.0", "YELLOW_BOLD"))
    warning = """
⚠️ WARNING - READ BEFORE RUNNING ⚠️

This program can download YouTube videos or any file links
using multithreading and YT-DLP (with ffmpeg support).

➤ It will:
  • Download multiple videos in parallel.
  • Show real-time progress bars in your terminal.
  • Auto-create folders for YouTube and files.
  • Use best video+audio stream up to 720p.

🚫 Disclaimer:
  • Use this script for personal or educational purposes only.
  • Do NOT use it to infringe copyrights or YouTube policies.

💡 Tip:
  • Ensure ffmpeg and yt-dlp are installed.
  • Windows users can set ffmpeg path at:  C:\\ffmpeg\\bin\\ffmpeg.exe
"""
    lines = warning.strip().splitlines()
    width = max(len(line) for line in lines) + 6
    print(colorize("=" * width, "RED_BOLD"))
    for line in lines:
        print(colorize("| " + line.ljust(width - 4) + " |", "RED_BOLD"))
    print(colorize("=" * width, "RED_BOLD"))
    choice = input(colorize("Press ENTER to continue or type 'exit' to quit: ", "YELLOW_BOLD")).strip().lower()
    if choice == "exit":
        print(colorize("❌ Program exited by user.", "GREEN_BOLD"))
        sys.exit(0)

# ────────────────────────────────
# 💡 BANNER & INFO
# ────────────────────────────────
def made_by():
    print(colorize("\n···············································································", "GREEN"))
    print(colorize(":.###....###...######.............######....#######..#########...########..########............................:","RED_BOLD"))
    print(colorize(":.####..####..##....##...........##....##..##.....##..##.....##..##........##.....##.........................:","RED_BOLD"))
    print(colorize(":.##..##..##..##.................##........##.....##..##.....##..##........##.....##...........................:","RED_BOLD"))
    print(colorize(":.##..#...##...######............##........##.....##..##.....##..#####.....##.####.............................:","RED_BOLD"))
    print(colorize(":.##......##........##...........##........##.....##..##.....##..##........##....##...............................:","RED_BOLD"))
    print(colorize(":.##......##..##....##...........##....##..##.....##..##.....##..##........##.....##..............................:","RED_BOLD"))
    print(colorize(":.##......##...######.............######....#######..#########...########..##.....##..........................:","RED_BOLD"))
    print(colorize("·················································································", "GREEN"))


# ────────────────────────────────
# 📦 CORE DOWNLOAD FUNCTIONS
# ────────────────────────────────
def move_cursor_to(line_num):
    sys.stdout.write(f"\033[{line_num};0H")

def progress_hook_generator(video_num):
    def hook(d):
        GREEN = '\033[92m'
        RESET = '\033[0m'
        line_number = (video_num - 1) * 3 + 2

        if d['status'] == 'downloading':
            total = d.get('total_bytes') or d.get('total_bytes_estimate') or 1
            downloaded = d.get('downloaded_bytes', 0)
            percent = downloaded / total if total > 1 else 0
            bar_length = 40
            filled_length = int(bar_length * percent)
            bar = '█' * filled_length + ' ' * (bar_length - filled_length)

            with print_lock:
                move_cursor_to(line_number)
                sys.stdout.write(f"{GREEN}{bar}{RESET} {percent * 100:5.1f}%")
                sys.stdout.flush()

        elif d['status'] == 'finished':
            with print_lock:
                move_cursor_to(line_number)
                sys.stdout.write(f"\r✅ Done{' ' * 40}\n")
                sys.stdout.flush()
    return hook

def normalize_url(url):
    if "youtu.be/" in url:
        video_id = url.split('/')[-1].split('?')[0]
        return f"https://www.youtube.com/watch?v={video_id}"
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    video_id = query.get("v", [None])[0]
    if video_id:
        return f"https://www.youtube.com/watch?v={video_id}"
    return url

def download_youtube_video(url, name):
    try:
        line_number = (name - 1) * 3 + 1
        os.makedirs("yt_videos", exist_ok=True)
        with print_lock:
            move_cursor_to(line_number)
            sys.stdout.write(f"🎬 Video {name}:\n")
            sys.stdout.flush()

        normalized_url = normalize_url(url)
        ydl_opts = {
            'outtmpl': f'yt_videos/video{name}.%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
            'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
            'quiet': True,
            'no_warnings': True,
            'noplaylist': False,
            'progress_hooks': [progress_hook_generator(name)],
        }

        if os.path.exists("C:\\ffmpeg\\bin\\ffmpeg.exe"):
            ydl_opts['ffmpeg_location'] = "C:\\ffmpeg\\bin\\ffmpeg.exe"

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([normalized_url])

        return f"✅ Video {name} downloaded successfully."

    except Exception as e:
        with print_lock:
            move_cursor_to(line_number)
            sys.stdout.write(f"❌ Error in video {name}: {e}\n")
            sys.stdout.flush()

def file_download(url, name):
    os.makedirs("file", exist_ok=True)
    try:
        print(f"📁 Downloading file {name}")
        response = requests.get(url, timeout=15)
        with open(f"file/file{name}.jpg", 'wb') as f:
            f.write(response.content)
        return f"✅ File {name} downloaded"
    except Exception as e:
        return f"❌ File {name} failed: {e}"

# ────────────────────────────────
# 🚀 MAIN EXECUTION
# ────────────────────────────────
if __name__ == "__main__":
    made_by()
    show_warning_box()

    t1 = time.time()
    print(colorize("\n1. YouTube Videos\n2. Web Images", "YELLOW_BOLD"))
    choice = input(colorize("Enter your choice: ", "CYAN_BOLD")).strip()

    if choice == "1":
        num = int(input(colorize("How many YouTube URLs (videos or playlists): ", "GREEN_BOLD")))
        urls = [input(colorize(f"Enter URL {i + 1}: ", "CYAN_BOLD")) for i in range(num)]
        names = [i + 1 for i in range(num)]
        print("\033c", end="")
        print("\n" * (num * 3))

        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = executor.map(lambda x: download_youtube_video(x[0], x[1]), zip(urls, names))
            for r in results:
                print(colorize(r, "GREEN_BOLD"))

    elif choice == "2":
        num = int(input(colorize("How many images to download: ", "GREEN_BOLD")))
        urls = [input(colorize(f"Enter image URL {i + 1}: ", "CYAN_BOLD")) for i in range(num)]
        names = [i + 1 for i in range(num)]
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = executor.map(file_download, urls, names)
            for r in results:
                print(colorize(r, "GREEN_BOLD"))
    else:
        print(colorize("Invalid choice!", "RED_BOLD"))

    print(colorize(f"\n⏱ Total time: {time.time() - t1:.2f} sec\n", "YELLOW_BOLD"))
