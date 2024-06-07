import os
import yt_dlp
import instaloader


# Функция для проверки и добавления протокола к URL
def ensure_protocol(url):
    if not url.startswith(('http://', 'https://')):
        return 'https://' + url
    return url


# Функция для получения имени канала на YouTube
def get_youtube_channel_name(url):
    ydl_opts = {'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            return info.get('uploader', 'Unknown Channel')
        except Exception as e:
            raise Exception(f"Error processing YouTube URL {url}: {e}")


# Функция для скачивания видео с YouTube
def download_youtube_videos(url, count=1):
    ydl_opts = {
        'quiet': True,
        'outtmpl': '%(title)s.%(ext)s',
        'format': 'best[ext=mp4]',
        'noplaylist': True,
        'max_downloads': count
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            return [f"{item['title']}.{item['ext']}" for item in
                    ydl.extract_info(url, download=False)['entries'][:count]]
        except Exception as e:
            raise Exception(f"Error downloading videos from {url}: {e}")


# Функция для получения имени профиля в Instagram
def get_instagram_profile_name(url):
    loader = instaloader.Instaloader()
    profile_name = url.split('/')[-2]
    profile = instaloader.Profile.from_username(loader.context, profile_name)
    return profile.full_name


# Функция для скачивания фотографий из Instagram
def download_instagram_photos(username, count=12):
    loader = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(loader.context, username)
    photos = []
    for post in profile.get_posts():
        if len(photos) >= count:
            break
        loader.download_post(post, target=f'./{username}')
        photos.append(post.url)
    return photos


# Функция для сохранения контента в папку
def save_content(name, description, instagram_photos, youtube_videos):
    folder_name = name.replace(" ", "_")
    os.makedirs(folder_name, exist_ok=True)

    # Сохранение текстовой информации
    with open(f"{folder_name}/description.txt", "w", encoding="utf-8") as f:
        f.write(description)

    # Сохранение URL скачанных фото
    with open(f"{folder_name}/photos.txt", "w", encoding="utf-8") as f:
        for photo in instagram_photos:
            f.write(photo + '\n')

    # Перемещение скачанных видео в папку
    for video in youtube_videos:
        video_path = video
        os.rename(video_path, f"{folder_name}/{os.path.basename(video_path)}")


# Основная функция
def main():
    with open('urls.txt', 'r') as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        if not url:
            continue

        url = ensure_protocol(url)

        try:
            if 'youtube.com' in url or 'youtu.be' in url:
                name = get_youtube_channel_name(url)
                description = f"YouTube channel: {name}"
                videos = download_youtube_videos(url)
                photos = []
            elif 'instagram.com' in url:
                name = get_instagram_profile_name(url)
                description = f"Instagram profile: {name}"
                photos = download_instagram_photos(url.split('/')[-2])
                videos = []
            else:
                # Если потребуется добавить парсинг для других сайтов
                raise NotImplementedError(f"Parsing for URL {url} is not implemented.")

            save_content(name, description, photos, videos)
        except Exception as e:
            print(f"Error processing {url}: {e}")


if __name__ == '__main__':
    main()
