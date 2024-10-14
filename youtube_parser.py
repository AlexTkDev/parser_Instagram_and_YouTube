import os
import yt_dlp

"""This module contains functions for downloading videos from YouTube."""


def ensure_protocol(url):
    """Ensure that the URL starts with http or https."""
    if not url.startswith(("http://", "https://")):
        return "https://" + url
    return url


def get_youtube_channel_name(url):
    """Get the full name of the YouTube channel from the URL."""
    ydl_opts = {"quiet": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            return info.get("uploader", "Unknown Channel")
        except yt_dlp.utils.DownloadError as e:
            raise yt_dlp.utils.DownloadError(f"Error processing YouTube URL {url}: {e}")


def download_youtube_videos(url, count=1):
    """Download videos from the specified YouTube URL."""
    ydl_opts = {
        "quiet": True,
        "outtmpl": "%(title)s.%(ext)s",
        "format": "best[ext=mp4]",
        "noplaylist": True,
        "max_downloads": count,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            info = ydl.extract_info(url, download=False)
            return [
                       f"{item['title']}.{item['ext']}" for item in info.get("entries", [info])
                   ][:count]
        except yt_dlp.utils.DownloadError as e:
            raise yt_dlp.utils.DownloadError(f"Error downloading videos from {url}: {e}")


def save_content(name, description, youtube_videos):
    """Save the YouTube channel name and description, as well as the URLs of downloaded videos."""
    folder_name = name.replace(" ", "_")
    os.makedirs(folder_name, exist_ok=True)

    with open(f"{folder_name}/description.txt", "w", encoding="utf-8") as f:
        f.write(description)

    for video in youtube_videos:
        video_path = video
        os.rename(video_path, f"{folder_name}/{os.path.basename(video_path)}")


def main():
    """Main function to download videos from YouTube."""
    with open("urls.txt", "r", encoding="utf-8") as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        if not url or ("youtube.com" not in url and "youtu.be" not in url):
            continue

        url = ensure_protocol(url)

        try:
            name = get_youtube_channel_name(url)
            description = f"YouTube channel: {name}"
            videos = download_youtube_videos(url)
            save_content(name, description, videos)
        except yt_dlp.utils.DownloadError as e:
            print(f"Error processing {url}: {e}")


if __name__ == "__main__":
    main()
