import os
import asyncio
from concurrent.futures import ThreadPoolExecutor  # Стандартный импорт должен идти раньше
import yt_dlp

"""Этот модуль содержит функции для загрузки видео с YouTube."""


def ensure_protocol(url):
    """Обеспечить, чтобы URL начинался с http или https."""
    if not url.startswith(("http://", "https://")):
        return "https://" + url
    return url


def get_youtube_channel_name(url):
    """Получить полное имя канала YouTube из URL."""
    ydl_opts = {"quiet": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            return info.get("uploader", "Неизвестный канал")
        except yt_dlp.utils.DownloadError as e:
            raise yt_dlp.utils.DownloadError(f"Ошибка при обработке URL YouTube {url}: {e}")


def download_youtube_videos(url, count=1):
    """Скачать указанное количество видео с YouTube."""
    ydl_opts = {
        "quiet": True,
        "outtmpl": "%(title)s.%(ext)s",
        "format": "best[ext=mp4]",
        "noplaylist": True,
        "max_downloads": count,  # Ограничить количество загружаемых видео
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)

            # Если это плейлист, получаем список видео
            entries = info.get("entries", [info])
            if entries:  # Сортировка по дате загрузки (если доступно)
                entries.sort(key=lambda x: x.get('upload_date', '0'), reverse=True)

                downloaded_videos = []
                for entry in entries[:count]:
                    video_url = entry.get('webpage_url')
                    if video_url:
                        ydl.download([video_url])
                        downloaded_videos.append(f"{entry['title']}.mp4")
                return downloaded_videos
            # Если это одиночное видео
            ydl.download([url])
            return [f"{info['title']}.mp4"]

        except yt_dlp.utils.MaxDownloadsReached:
            print(f"Достигнуто максимальное количество загрузок для {url}.")
            return []
        except yt_dlp.utils.DownloadError as e:
            raise yt_dlp.utils.DownloadError(f"Ошибка при загрузке видео с {url}: {e}")


def save_content(name, description, youtube_videos):
    """Сохранить имя канала YouTube и описание, а также URL загруженных видео."""
    folder_name = name.replace(" ", "_")
    os.makedirs(folder_name, exist_ok=True)

    with open(f"{folder_name}/description.txt", "w", encoding="utf-8") as f:
        f.write(description)

    for video in youtube_videos:
        video_path = video
        # Переименовать файл, чтобы он оказался в нужной папке
        os.rename(video_path, f"{folder_name}/{os.path.basename(video_path)}")


async def download_video_async(url, executor, count):
    """Асинхронно скачать видео."""
    loop = asyncio.get_event_loop()
    try:
        name = await loop.run_in_executor(executor, get_youtube_channel_name, url)
        description = f"YouTube канал: {name}"
        videos = await loop.run_in_executor(executor, download_youtube_videos, url, count)
        save_content(name, description, videos)
    except yt_dlp.utils.DownloadError as e:
        print(f"Ошибка при обработке {url}: {e}")


async def main():
    """Основная функция для загрузки видео с YouTube."""
    with open("urls.txt", "r", encoding="utf-8") as file:
        urls = file.readlines()

    executor = ThreadPoolExecutor(max_workers=3)

    tasks = []
    for url in urls:
        url = url.strip()
        if not url or ("youtube.com" not in url and "youtu.be" not in url):
            continue

        url = ensure_protocol(url)

        # Количество видео для загрузки
        count = 3
        tasks.append(download_video_async(url, executor, count))

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
