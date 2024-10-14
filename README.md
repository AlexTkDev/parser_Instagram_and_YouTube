## YouTube and Instagram Parsers

### Overview

This project includes two scripts: one for downloading videos from YouTube and the other
for downloading photos from Instagram. Both scripts process URLs from the `urls.txt` file,
where each URL points to a YouTube channel or Instagram profile.

### Installation

1. Ensure that you have Python 3.12.0 or later installed.
2. Create and activate a virtual environment:
   **For Windows**:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   **For Unix**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install the required dependencies from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

### Checking and Installing ffmpeg

To avoid warnings about `ffmpeg` not being found, you should install it. Follow the
instructions for your operating system:

- **For macOS**: Use Homebrew:
  ```bash
  brew install ffmpeg
  ```
- **For Ubuntu/Debian**:
  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```
- **For Windows**: Download and install `ffmpeg` from
  the [official website](https://ffmpeg.org/download.html).

### Usage

#### `urls.txt` File

Add the YouTube channel URLs and Instagram profile URLs you want to process
to the `urls.txt` file. Each URL should be on a new line. Example content:

```
https://www.instagram.com/diachenko.tattoo/
https://www.youtube.com/@user-me5tu9kk1t
```

#### Running the YouTube Parser

To run the YouTube parser script, execute the following command:

```bash
python youtube_parser.py
```

The script will process all URLs containing `youtube.com` or `youtu.be` and download videos from
the listed channels.

#### Running the Instagram Parser

To run the Instagram parser script, use the following command:

```bash
python instagram_parser.py
```

The script will process all URLs containing `instagram.com` and download photos from the listed
profiles.

### Output

- **YouTube Parser**: The downloaded videos are saved in folders named after the channel. Each
  folder contains a `description.txt` file with channel information.
- **Instagram Parser**: The photos are saved in folders named after the profile. Each folder
  contains a `description.txt` file with profile information and a `photos.txt` file listing the
  downloaded photo URLs.

### Code Quality Check

To ensure the code follows PEP8 standards, use `pylint`. For example:

```bash
pylint --disable=missing-module-docstring,missing-function-docstring,pointless-string-statement youtube_parser.py
```

You can similarly check the Instagram script.

### Note

Make sure to use the scripts in compliance with the terms of service of YouTube and Instagram.

***

## Парсеры для YouTube и Instagram

### Описание

Данный проект состоит из двух скриптов: один для загрузки видео с YouTube, другой для загрузки
фотографий с Instagram. Оба скрипта обрабатывают URL-адреса из файла `urls.txt`, где каждый URL
указывает на канал YouTube или профиль Instagram.

### Установка

1. Убедитесь, что у вас установлен Python 3.12.0 или выше.
2. Создайте и активируйте виртуальное окружение:
   **Для Windows**:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   **Для Unix**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Установите необходимые зависимости из файла `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

### Проверка и установка ffmpeg

Чтобы избежать предупреждений о том, что `ffmpeg` не найден, вам следует установить его. Следуйте
инструкции для вашей операционной системы:

- **Для macOS**: Используйте Homebrew:
  ```bash
  brew install ffmpeg
  ```
- **Для Ubuntu/Debian**:
  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```
- **Для Windows**: Скачайте и установите `ffmpeg`
  с [официального сайта](https://ffmpeg.org/download.html).

### Использование

#### Файл `urls.txt`

Добавьте URL-адреса YouTube каналов и Instagram профилей, которые вы хотите обработать, в файл
`urls.txt`. Каждый URL должен быть на новой строке. Пример содержимого файла:

```
https://www.instagram.com/diachenko.tattoo/
https://www.youtube.com/@user-me5tu9kk1t
```

#### Запуск YouTube парсера

Для запуска скрипта YouTube парсера выполните следующую команду:

```bash
python youtube_parser.py
```

Скрипт обработает все URL-адреса, содержащие `youtube.com` или `youtu.be`, и загрузит видео с
указанных каналов.

#### Запуск Instagram парсера

Для запуска скрипта Instagram парсера выполните команду:

```bash
python instagram_parser.py
```

Скрипт обработает все URL-адреса, содержащие `instagram.com`, и скачает фотографии с указанных
профилей.

### Результаты

- **YouTube парсер**: Загруженные видео сохраняются в папки, названные по имени канала. В каждой
  папке создается файл `description.txt` с описанием канала.
- **Instagram парсер**: Фотографии сохраняются в папки, названные по имени профиля. В каждой папке
  создается файл `description.txt` с описанием профиля и файл `photos.txt` с ссылками на скачанные
  фотографии.

### Проверка качества кода

Для проверки кода на соответствие стандартам PEP8 используйте `pylint`. Например:

```bash
pylint --disable=missing-module-docstring,missing-function-docstring,pointless-string-statement youtube_parser.py
```

Точно так же можно проверить и скрипт для Instagram.

### Примечание

Убедитесь, что используете скрипты в соответствии с условиями использования платформ YouTube и
Instagram.