import os
import instaloader
import asyncio
from concurrent.futures import ThreadPoolExecutor


# Функция для проверки и добавления протокола к URL
def ensure_protocol(url):
    if not url.startswith(("http://", "https://")):
        return "https://" + url
    return url


# Функция для получения имени профиля в Instagram
def get_instagram_profile_name(url):
    loader = instaloader.Instaloader()
    profile_name = url.split("/")[-2]  # Извлекаем имя пользователя из URL
    profile = instaloader.Profile.from_username(loader.context, profile_name)
    return profile.full_name


# Асинхронная обертка для скачивания фотографий
async def download_instagram_photos(username, count=12):
    loop = asyncio.get_event_loop()
    photos = []

    with ThreadPoolExecutor() as executor:
        loader = instaloader.Instaloader()
        profile = await loop.run_in_executor(executor, instaloader.Profile.from_username,
                                             loader.context, username)

        for post in profile.get_posts():
            if len(photos) >= count:
                break
            # Указываем целевой путь для загрузки фотографий
            await loop.run_in_executor(executor, loader.download_post, post,
                                       f"result/{username}")  # Загружаем в нужную папку
            photos.append(post.url)

    return photos


# Функция для сохранения контента в папку
def save_content(name, description, instagram_photos):
    folder_name = os.path.join("result", name.replace(" ", "_"))
    os.makedirs(folder_name, exist_ok=True)

    # Сохраняем текстовое описание
    with open(os.path.join(folder_name, "description.txt"), "w", encoding="utf-8") as f:
        f.write(description)

    # Сохраняем URL скачанных фотографий
    with open(os.path.join(folder_name, "photos.txt"), "w", encoding="utf-8") as f:
        for photo in instagram_photos:
            f.write(photo + "\n")


# Основная асинхронная функция
async def main():
    with open("urls.txt", "r") as file:
        urls = file.readlines()

    tasks = []

    for url in urls:
        url = url.strip()
        if not url or "instagram.com" not in url:
            continue  # Игнорируем неподходящие URL

        url = ensure_protocol(url)

        try:
            name = get_instagram_profile_name(url)
            description = f"Instagram profile: {name}"
            tasks.append(download_instagram_photos(url.split("/")[-2]))

            # Сохраняем контент асинхронно
            photos = await tasks[-1]  # Ждем завершения задачи
            save_content(name, description, photos)

        except Exception as e:
            print(f"Error processing {url}: {e}")


if __name__ == "__main__":
    os.makedirs("result", exist_ok=True)  # Создаем родительскую папку "result"
    asyncio.run(main())
