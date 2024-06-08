# Парсеры для YouTube и Instagram

## Описание

Эти два скрипта позволяют загружать контент с YouTube и Instagram. Каждый скрипт работает с файлом `urls.txt`, который
содержит список URL-адресов для обработки. YouTube парсер скачивает видео, а Instagram парсер загружает фотографии.

## Установка

1. Убедитесь, что у вас установлен Python 3.7 или выше.
2. Установите необходимые пакеты с помощью pip:

   python -m venv venv

   venv\Scripts\activate (для Windows)

   source venv/bin/activate (для Unix)


3. Установите необходимые пакеты из requirements.txt:

   pip install -r requirements.txt

## Использование

Файл urls.txt
В этот файл добавьте URL-адреса YouTube каналов и Instagram
профилей, которые вы хотите обработать. Каждый URL должен быть на новой строке. Пример содержимого:

https://www.instagram.com/diachenko.tattoo/

https://www.youtube.com/@user-me5tu9kk1t

## Запуск YouTube парсера

Для запуска скрипта YouTube парсера выполните команду:

    python youtube_parser.py

Скрипт обработает все URL-адреса, содержащие youtube.com или youtu.be, и загрузит видео с указанных каналов.

Запуск Instagram парсера
Для запуска скрипта Instagram парсера выполните команду:

    python instagram_parser.py

Скрипт обработает все URL-адреса, содержащие instagram.com, и загрузит фотографии с указанных профилей.

## Результаты

Результаты работы скриптов сохраняются в папки, названные по имени канала или профиля.
В каждой папке создается файл description.txt с описанием и, соответственно, файл photos.txt или загруженные видеофайлы.