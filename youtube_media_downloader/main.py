#!/usr/bin/env python3
"""
YouTube Downloader with Logging
Enhanced version supporting both video and audio downloads
"""
from pytube import YouTube
from datetime import datetime
from tqdm import tqdm
import os
import sys
import argparse


def setup_directories():
    """Create output directories if they don't exist"""
    os.makedirs('output/videos', exist_ok=True)
    os.makedirs('output/audio', exist_ok=True)


def log_message(log_file, message, error=False):
    """Write message to log file"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if error:
        log_file.write(f'{"="*60}\n')
        log_file.write(f'ERROR - {timestamp}\n')
        log_file.write(f'{message}\n')
        log_file.write(f'{"="*60}\n\n')
    else:
        log_file.write(f'{timestamp} - {message}\n')


def download_video(url, output_path, log_file, quality='highest'):
    """Download video from YouTube URL"""
    try:
        yt = YouTube(url)
        log_message(log_file, f'Downloading video: {yt.title}')
        
        # Get video stream
        if quality == 'highest':
            stream = yt.streams.get_highest_resolution()
        else:
            stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        
        if not stream:
            raise ValueError("No suitable video stream found")
        
        # Download
        stream.download(output_path=output_path)
        log_message(log_file, f'Completed: {yt.title}\n')
        return True
        
    except Exception as e:
        log_message(log_file, f'{url}\nError: {str(e)}', error=True)
        return False


def download_audio(url, output_path, log_file):
    """Download audio only from YouTube URL"""
    try:
        yt = YouTube(url)
        log_message(log_file, f'Downloading audio: {yt.title}')
        
        # Get audio stream
        stream = yt.streams.filter(only_audio=True).first()
        
        if not stream:
            raise ValueError("No audio stream found")
        
        # Download
        stream.download(output_path=output_path)
        log_message(log_file, f'Completed: {yt.title}\n')
        return True
        
    except Exception as e:
        log_message(log_file, f'{url}\nError: {str(e)}', error=True)
        return False


def process_urls(source_file, mode='video', quality='highest'):
    """Process URLs from source file"""
    setup_directories()
    
    # Determine output path
    output_path = 'output/videos' if mode == 'video' else 'output/audio'
    
    # Read URLs
    try:
        with open(source_file, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: {source_file} not found!")
        print("Create a 'source.txt' file with YouTube URLs (one per line)")
        return
    
    if not urls:
        print(f"No URLs found in {source_file}")
        return
    
    # Process downloads
    log_filename = f'logs_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
    
    with open(log_filename, 'w') as log_file:
        log_message(log_file, f'Started {mode} download session')
        log_message(log_file, f'Total URLs: {len(urls)}\n')
        
        success_count = 0
        fail_count = 0
        
        print(f"\nDownloading {len(urls)} URLs as {mode}...\n")
        
        for url in tqdm(urls, desc="Progress"):
            if mode == 'video':
                success = download_video(url, output_path, log_file, quality)
            else:
                success = download_audio(url, output_path, log_file)
            
            if success:
                success_count += 1
            else:
                fail_count += 1
        
        # Summary
        log_message(log_file, f'\n{"="*60}')
        log_message(log_file, 'SUMMARY')
        log_message(log_file, f'Total: {len(urls)}')
        log_message(log_file, f'Success: {success_count}')
        log_message(log_file, f'Failed: {fail_count}')
        log_message(log_file, f'{"="*60}')
        
        print(f"\n{'='*60}")
        print(f"Download complete!")
        print(f"Success: {success_count} | Failed: {fail_count}")
        print(f"Log saved to: {log_filename}")
        print(f"Files saved to: {output_path}")
        print(f"{'='*60}\n")


def main():
    parser = argparse.ArgumentParser(
        description='YouTube Downloader with logging support',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                          # Download videos (default)
  python main.py --mode audio             # Download audio only
  python main.py --mode video --quality lowest    # Download lowest quality video
  python main.py --source my_urls.txt     # Use custom source file
        """
    )
    
    parser.add_argument(
        '--mode', 
        choices=['video', 'audio'], 
        default='video',
        help='Download mode: video or audio (default: video)'
    )
    
    parser.add_argument(
        '--quality',
        choices=['highest', 'lowest'],
        default='highest',
        help='Video quality: highest or lowest (default: highest, only for video mode)'
    )
    
    parser.add_argument(
        '--source',
        default='source.txt',
        help='Source file containing YouTube URLs (default: source.txt)'
    )
    
    args = parser.parse_args()
    
    print("\n" + "="*60)
    print("YouTube Downloader with Logging")
    print("="*60)
    print(f"Mode: {args.mode.upper()}")
    if args.mode == 'video':
        print(f"Quality: {args.quality}")
    print(f"Source: {args.source}")
    print("="*60 + "\n")
    
    process_urls(args.source, args.mode, args.quality)


if __name__ == '__main__':
    main()
