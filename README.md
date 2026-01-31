# YouTube Downloader with Logging

A Python tool to download YouTube videos or audio with comprehensive logging.

## Features

- 📹 Download videos (highest or lowest quality)
- 🎵 Download audio only
- 📝 Automatic logging with timestamps
- 📊 Progress bar for batch downloads
- ✅ Success/failure tracking
- 📁 Organized output folders

## Installation

### Option 1: Install from PyPI (Recommended)

```bash
pip install youtube-media-downloader
```

### Option 2: Install from Source

```bash
git clone https://github.com/lukaszplk/youtube-media-downloader.git
cd youtube-media-downloader
pip install -r requirements.txt
```

## Usage

### Create Source File

Create a `source.txt` file with YouTube URLs (one per line):

```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://www.youtube.com/watch?v=9bZkp7q19f0
```

### Download Videos (Default)

```bash
# If installed from PyPI
youtube-downloader

# If running from source
python -m youtube_media_downloader.main
```

### Download Audio Only

```bash
# If installed from PyPI
youtube-downloader --mode audio

# If running from source
python -m youtube_media_downloader.main --mode audio
```

### Download Lowest Quality Video

```bash
python main.py --mode video --quality lowest
```

### Use Custom Source File

```bash
youtube-downloader --source my_urls.txt
```

## Output Structure

```
output/
├── videos/     # Downloaded videos
└── audio/      # Downloaded audio files

logs_YYYYMMDD_HHMMSS.txt  # Session log
```

## Options

```
--mode {video,audio}       Download mode (default: video)
--quality {highest,lowest} Video quality (default: highest)
--source FILE              Source file path (default: source.txt)
```

## Example

```bash
# Download 10 videos in highest quality
python main.py

# Download audio for music playlist
python main.py --mode audio --source playlist.txt

# Download low quality for preview
python main.py --quality lowest
```

## Log Format

Each session creates a timestamped log file with:
- Download start/completion times
- Success/failure status
- Error messages for failed downloads
- Summary statistics

## License

MIT License - Free to use and modify
