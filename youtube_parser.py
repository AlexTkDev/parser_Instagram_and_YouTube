import os
import yt_dlp


# Функция для проверки и добавления протокола к URL
def ensure_protocol(url):
    if not url.startswith(("http://", "https://")):
        return "https://" + url
    return url


# Функция для получения имени канала на YouTube
def get_youtube_channel_name(url):
    ydl_opts = {"quiet": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            # Извлекаем информацию о канале, не загружая видео
            info = ydl.extract_info(url, download=False)
            return info.get("uploader", "Unknown Channel")
        except Exception as e:
            raise Exception(f"Error processing YouTube URL {url}: {e}")


# Функция для скачивания видео с YouTube
def download_youtube_videos(url, count=1):
    ydl_opts = {
        "quiet": True,
        "outtmpl": "%(title)s.%(ext)s",  # Шаблон для имен файлов
        "format": "best[ext=mp4]",  # Формат видео
        "noplaylist": True,  # Игнорировать плейлисты
        "max_downloads": count,  # Максимальное количество загружаемых видео
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            # Загружаем видео и возвращаем список загруженных файлов
            ydl.download([url])
            info = ydl.extract_info(url, download=False)
            return [
                       f"{item['title']}.{item['ext']}" for item in info.get("entries", [info])
                   ][:count]
        except Exception as e:
            raise Exception(f"Error downloading videos from {url}: {e}")


# Функция для сохранения контента в папку
def save_content(name, description, youtube_videos):
    folder_name = name.replace(" ", "_")
    os.makedirs(folder_name, exist_ok=True)

    # Сохраняем текстовое описание
    with open(f"{folder_name}/description.txt", "w", encoding="utf-8") as f:
        f.write(description)

    # Перемещаем загруженные видео в папку
    for video in youtube_videos:
        video_path = video
        os.rename(video_path, f"{folder_name}/{os.path.basename(video_path)}")


# Основная функция
def main():
    with open("urls.txt", "r") as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        if not url or ("youtube.com" not in url and "youtu.be" not in url):
            continue  # Игнорируем неподходящие URL

        url = ensure_protocol(url)

        try:
            name = get_youtube_channel_name(url)
            description = f"YouTube channel: {name}"
            videos = download_youtube_videos(url)
            save_content(name, description, videos)
        except Exception as e:
            print(f"Error processing {url}: {e}")


if __name__ == "__main__":
    main()
