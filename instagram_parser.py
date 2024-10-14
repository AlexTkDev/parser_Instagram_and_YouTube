import os
import asyncio
from concurrent.futures import ThreadPoolExecutor
import instaloader

"""This module contains functions for downloading photos from Instagram."""


def ensure_protocol(url):
    """Ensure that the URL starts with http or https."""
    if not url.startswith(("http://", "https://")):
        return "https://" + url
    return url


def get_instagram_profile_name(url):
    """Get the full name of the Instagram profile from the URL."""
    loader = instaloader.Instaloader()
    profile_name = url.split("/")[-2]
    profile = instaloader.Profile.from_username(loader.context, profile_name)
    return profile.full_name


async def download_instagram_photos(username, count=12):
    """Download photos from the specified Instagram profile."""
    loop = asyncio.get_event_loop()
    photos = []

    with ThreadPoolExecutor() as executor:
        loader = instaloader.Instaloader()
        profile = await loop.run_in_executor(executor, instaloader.Profile.from_username,
                                             loader.context, username)

        for post in profile.get_posts():
            if len(photos) >= count:
                break
            await loop.run_in_executor(executor, loader.download_post, post,
                                       f"result/{username}")
            photos.append(post.url)

    return photos


def save_content(name, description, instagram_photos):
    """Save the profile name and description, as well as the URLs of downloaded photos."""
    folder_name = os.path.join("result", name.replace(" ", "_"))
    os.makedirs(folder_name, exist_ok=True)

    with open(os.path.join(folder_name, "description.txt"), "w", encoding="utf-8") as f:
        f.write(description)

    with open(os.path.join(folder_name, "photos.txt"), "w", encoding="utf-8") as f:
        for photo in instagram_photos:
            f.write(photo + "\n")


async def main():
    """Main function to download photos from Instagram."""
    with open("urls.txt", "r", encoding="utf-8") as file:
        urls = file.readlines()

    tasks = []

    for url in urls:
        url = url.strip()
        if not url or "instagram.com" not in url:
            continue

        url = ensure_protocol(url)

        try:
            name = get_instagram_profile_name(url)
            description = f"Instagram profile: {name}"
            tasks.append(download_instagram_photos(url.split("/")[-2]))

            photos = await tasks[-1]
            save_content(name, description, photos)

        except instaloader.exceptions.InstaloaderException as e:
            print(f"Error processing {url}: {e}")


if __name__ == "__main__":
    os.makedirs("result", exist_ok=True)
    asyncio.run(main())
