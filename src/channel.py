import json
import os
import isodate

from googleapiclient.discovery import build

import isodate

from helper.youtube_api_manual import printj

class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, __channel_id: str, channel_name, chanel_description, channel_link, number_of_subscribers, number_of_videos, total_views) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = str(__channel_id)
        self.channel_name = channel_name
        self.chanel_description = chanel_description
        self.channel_link = channel_link
        self.number_of_subscribers = number_of_subscribers
        self.number_of_videos = number_of_videos
        self.total_views = total_views

    def print_info(self, dict_to_print, indent, ensure_asci) -> None:
        """Выводит в консоль информацию о канале."""
        return json.dumps(dict_to_print, indent=2, ensure_ascii=False)

    @classmethod
    def get_service(cls):
        return Channel

    def to_json(title, video_count, url):
        file = open("file.json", "w")
        file.write(title, video_count, url)
        return file

    def __str__(self):
        """Выведение названия канала и ссылки"""
        return f'{self.channel_name}, {self.channel_link}'

    def __add__(self, other):
        """Метод для сложения колличества подписчиков каналов"""
        return self.number_of_subscribers + other.number_of_subscribers

    def __sub__(self, other):
        """Метод для операции вычитания"""
        return self.number_of_subscribers - other.number_of_subscribers

    def __lt__(self, other):
        """Для операции сравнения «меньше»"""
        return self.number_of_subscribers < other.number_of_subscribers

    def __le__(self, other):
        """Для сравнения «меньше» или «равно»"""
        return self.number_of_subscribers <= other.number_of_subscribers

    def __gt__(self, other):
        """Метод для операции сравнения «больше»"""
        return self.number_of_subscribers > other.number_of_subscribers

    def __ge__(self, other):
        """Метод для операции сравнения «больше» или «равно»"""
        return self.number_of_subscribers >= other.number_of_subscribers


