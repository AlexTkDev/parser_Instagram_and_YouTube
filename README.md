# Parsers for YouTube and Instagram

## Description

These two scripts allow you to download content from YouTube and Instagram. Each script works with the `urls.txt` file,
which contains a list of URLs to process. The YouTube parser downloads videos, while the Instagram parser downloads
photos.

## Installation

1. Ensure you have Python 3.12.0 or higher installed.
2. Install the required packages using pip:

```bash
   python -m venv venv

   venv\Scripts\activate (for Windows)

   source venv/bin/activate (for Unix)
```

3. Install the required packages from `requirements.txt`:

```bash
   pip install -r requirements.txt
```

## Usage

### `urls.txt` File

Add the URLs of YouTube channels and Instagram profiles you want to process to this file. Each URL should be on a new
line. Example content:

```
https://www.instagram.com/diachenko.tattoo/
https://www.youtube.com/@user-me5tu9kk1t
```

### Running the YouTube Parser

To run the YouTube parser script, execute the command:

```bash
    python youtube_parser.py
```

The script will process all URLs containing `youtube.com` or `youtu.be` and download videos from the specified channels.

### Running the Instagram Parser

To run the Instagram parser script, execute the command:

```bash
    python instagram_parser.py
```

The script will process all URLs containing `instagram.com` and download photos from the specified profiles.

## Results

The results of the scripts are saved in folders named after the channel or profile. Each folder contains
a `description.txt` file with a description and either a `photos.txt` file or the downloaded video files.

***

# Парсеры для YouTube и Instagram

## Описание

Эти два скрипта позволяют загружать контент с YouTube и Instagram. Каждый скрипт работает с файлом `urls.txt`, который
содержит список URL-адресов для обработки. YouTube парсер скачивает видео, а Instagram парсер загружает фотографии.

## Установка

1. Убедитесь, что у вас установлен Python 3.12.0 или выше.
2. Установите необходимые пакеты с помощью pip:

```bash
   python -m venv venv

   venv\Scripts\activate (для Windows)

   source venv/bin/activate (для Unix)
```

3. Установите необходимые пакеты из requirements.txt:

```bash
   pip install -r requirements.txt
```

## Использование

Файл urls.txt
В этот файл добавьте URL-адреса YouTube каналов и Instagram
профилей, которые вы хотите обработать. Каждый URL должен быть на новой строке. Пример содержимого:

https://www.instagram.com/diachenko.tattoo/

https://www.youtube.com/@user-me5tu9kk1t

## Запуск YouTube парсера

Для запуска скрипта YouTube парсера выполните команду:

```bash
    python youtube_parser.py
```

Скрипт обработает все URL-адреса, содержащие youtube.com или youtu.be, и загрузит видео с указанных каналов.

Запуск Instagram парсера
Для запуска скрипта Instagram парсера выполните команду:

```bash
    python instagram_parser.py
```

Скрипт обработает все URL-адреса, содержащие instagram.com, и загрузит фотографии с указанных профилей.

## Результаты

Результаты работы скриптов сохраняются в папки, названные по имени канала или профиля.
В каждой папке создается файл description.txt с описанием и, соответственно, файл photos.txt или загруженные видеофайлы.
