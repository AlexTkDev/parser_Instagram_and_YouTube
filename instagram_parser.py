import os
import instaloader


# Функция для проверки и добавления протокола к URL
def ensure_protocol(url):
    if not url.startswith(('http://', 'https://')):
        return 'https://' + url
    return url


# Функция для получения имени профиля в Instagram
def get_instagram_profile_name(url):
    loader = instaloader.Instaloader()
    profile_name = url.split('/')[-2]  # Извлекаем имя пользователя из URL
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
def save_content(name, description, instagram_photos):
    folder_name = name.replace(" ", "_")
    os.makedirs(folder_name, exist_ok=True)

    # Сохраняем текстовое описание
    with open(f"{folder_name}/description.txt", "w", encoding="utf-8") as f:
        f.write(description)

    # Сохраняем URL скачанных фотографий
    with open(f"{folder_name}/photos.txt", "w", encoding="utf-8") as f:
        for photo in instagram_photos:
            f.write(photo + '\n')


# Основная функция
def main():
    with open('urls.txt', 'r') as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        if not url or 'instagram.com' not in url:
            continue  # Игнорируем неподходящие URL

        url = ensure_protocol(url)

        try:
            name = get_instagram_profile_name(url)
            description = f"Instagram profile: {name}"
            photos = download_instagram_photos(url.split('/')[-2])
            save_content(name, description, photos)
        except Exception as e:
            print(f"Error processing {url}: {e}")


if __name__ == '__main__':
    main()
