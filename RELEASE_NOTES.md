## 🎉 First Release - Enhanced YouTube Media Downloader

### ✨ Features
- **Video Download** - Download videos in highest or lowest quality
- **Audio Download** - Extract audio-only from YouTube videos
- **CLI Interface** - Easy command-line arguments (--mode, --quality, --source)
- **Batch Processing** - Download multiple videos from a source file
- **Comprehensive Logging** - Timestamped logs with success/failure tracking
- **Progress Tracking** - Visual progress bar with tqdm
- **Organized Output** - Separate folders for videos and audio

### 📦 Installation

```bash
pip install -r requirements.txt
```

### 🚀 Quick Start

```bash
# Download videos (default)
python main.py

# Download audio only
python main.py --mode audio

# Use custom source file
python main.py --source my_urls.txt
```

### 📚 Documentation
See [README.md](https://github.com/lukaszplk/youtube-media-downloader/blob/main/README.md) for full documentation and examples.

---
**Full Changelog**: First release with merged functionality from separate video and audio downloaders.
